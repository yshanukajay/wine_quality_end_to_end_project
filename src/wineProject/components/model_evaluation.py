import os
from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from src.wineProject.entity.config_entity import ModelEvaluationConfig
from src.wineProject.utils.common import save_json

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/YohanJay23/wine_quality_end_to_end_project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "YohanJay23"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "12aa8bae310f0795c7c23dcd43e1bb74fec38ea1"


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, predicted) -> tuple:
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_X = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_X)
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            scores ={   
                "rmse": rmse,
                "mae": mae,
                "r2": r2
            }
            
            save_json(path= Path(self.config.metrics_file_path), data=scores)
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metrics(scores)
            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model" ,registered_model_name="ElasticNetWineModel")
            else:
                mlflow.sklearn.log_model(model, "model")
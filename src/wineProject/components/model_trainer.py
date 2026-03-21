import pandas as pd
import os
from src.wineProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.wineProject.entity.config_entity import ModelTrainerConfig
from src.wineProject.utils.common import create_directories


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train_model(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        logger.info(f"Train data and test data are loaded successfully.")
        
        train_x = train_data.drop(self.config.target_col, axis=1)
        train_y = train_data[self.config.target_col]
        
        test_x = test_data.drop(self.config.target_col, axis=1)
        test_y = test_data[self.config.target_col]
        logger.info(f"Splitting of data into dependent and independent features is done successfully.")
        
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ration, random_state=42)
        model.fit(train_x, train_y)
        logger.info(f"Model training is done successfully.")
        
        model_dir = os.path.join(self.config.root_dir, self.config.model_name)
        create_directories([self.config.root_dir])
        joblib.dump(model, model_dir)
        logger.info(f"Model is saved at {model_dir} successfully.")
        
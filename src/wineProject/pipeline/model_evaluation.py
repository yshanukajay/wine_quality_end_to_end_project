from src.wineProject.config.configuration import ConfigurationManager
from src.wineProject.components.model_evaluation import ModelEvaluation
from src.wineProject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=evaluation_config)
        model_evaluation.log_into_mlflow()
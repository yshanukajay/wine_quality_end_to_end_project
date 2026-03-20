import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.wineProject import logger
from src.wineProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
        
        train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Train and test sets created at {self.config.root_dir}")
        logger.info(f"Train set shape: {train_set.shape}, Test set shape: {test_set.shape}")
        
        print(f"Train set shape: {train_set.shape}, Test set shape: {test_set.shape}")
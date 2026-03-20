import os
from urllib import request as requests
import zipfile
from src.wineProject import logger
from src.wineProject.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = requests.urlretrieve(
                self.config.source_URL, 
                self.config.local_data_file
            )
            logger.info(f"Data downloaded successfully to {self.config.local_data_file}")
        else:
            logger.info(f"Data already exists at {self.config.local_data_file}")
            
    def extract_zip_file(self):
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Data extracted successfully to {unzip_path}")
            
            
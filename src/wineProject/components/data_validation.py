import os
import pandas as pd
from src.wineProject.utils.common import create_directories
from src.wineProject import logger
from src.wineProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config = DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self):
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_dir)
            all_columns = list(data.columns)

            all_schema_columns = list(self.config.all_schema.keys())
     
            for col in all_columns:
                if col not in all_schema_columns:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation status: {validation_status}") 
                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation status: {validation_status}")
        except Exception as e:
            logger.exception(e)            

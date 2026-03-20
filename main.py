from src.wineProject import logger
from src.wineProject.pipeline.data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(f"Exception occurred in stage {STAGE_NAME}: {e}")
        raise e
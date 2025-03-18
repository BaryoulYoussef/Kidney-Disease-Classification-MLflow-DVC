from cnnClassifier.pipeline import stage_01_data_ingestion
from cnnClassifier import logger

STAGE_NAME ="Data ingestion stage"
try : 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<")
    obj = stage_01_data_ingestion.DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<<<<<<<<<< \n\nx========x")
except Exception as e :
    logger.exception(e)
    raise e
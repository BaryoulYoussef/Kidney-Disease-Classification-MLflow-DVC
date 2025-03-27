from cnnClassifier.pipeline import stage_01_data_ingestion
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
"""STAGE_NAME ="Data ingestion stage"
try : 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<")
    obj = stage_01_data_ingestion.DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<<<<<<<<<< \n\nx========x")
except Exception as e :
    logger.exception(e)
    raise e
"""


STAGE_NAME ="Prepare base model"

try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<<<<<<<<< \n\nx========x")

    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<<<<<<<<<< \n\nx========x")
except Exception as e :
    logger.exception(e)
    raise e


STAGE_NAME ="Training"

try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<<<<<<<<< \n\nx========x")

    model_trainer =ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<<<<<<<<<< \n\nx========x")
except Exception as e :
    logger.exception(e)
    raise e


STAGE_NAME ="Model Evaluation stage "

try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<<<<<<<<< \n\nx========x")

    model_evaluation =EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<<<<<<<<<< \n\nx========x")
except Exception as e :
    logger.exception(e)
    raise e



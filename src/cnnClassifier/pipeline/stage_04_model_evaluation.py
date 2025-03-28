from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger


STAGE_NAME="Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        #evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"*********************************")
        logger.info(f">>>>>>>>>>>>>>>>>stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<<<<<<\n\n x===================")
    except Exception as e :
        raise e 


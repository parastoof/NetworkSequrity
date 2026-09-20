from networksequrity.components.data_ingestion import DataIngestion
from networksequrity.components.data_validation import DataValidation
from networksequrity.components.data_transformation import DataTransformation
from networksequrity.components.model_trainer import ModelTrainer
from networksequrity.exception.exception import NetworkSecurityException
from networksequrity.logging.logger import logging
from networksequrity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksequrity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ =='__main__': 
    try: 
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation Compeleted")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("Start data transformation")
        data_transformation=DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_validation_artifact)
        logging.info("Data transformation Compeleted")

        logging.info("Model training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config, data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        print(data_validation_artifact)
        logging.info("Model training artifact Created")

        
    except Exception as e: 
        raise NetworkSecurityException(e,sys) 
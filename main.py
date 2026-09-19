from networksequrity.components.data_ingestion import DataIngestion
from networksequrity.components.data_validation import DataValidation

from networksequrity.exception.exception import NetworkSecurityException
from networksequrity.logging.logger import logging
from networksequrity.entity.config_entity import DataIngestionConfig, DataValidationConfig
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
        
    except Exception as e: 
        raise NetworkSecurityException(e,sys) 
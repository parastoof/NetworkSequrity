from networksequrity.components.data_ingestion import DataIngestion
from networksequrity.exception.exception import NetworkSecurityException
from networksequrity.logging.logger import logging
from networksequrity.entity.config_entity import DataIngestionConfig
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
    except Exception as e: 
        raise NetworkSecurityException(e,sys) 
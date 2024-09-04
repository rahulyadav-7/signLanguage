import sys, os
from signLangugae.logger import logging
from signLangugae.exception import SignException
from signLangugae.components.data_ingestion import DataIngestion
from signLangugae.entity.config_entity import DataIngestionConfig
from signLangugae.entity.artifcats_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from URL")

            # Create an instance of DataIngestion
            data_ingestion = DataIngestion(self.data_ingestion_config)
            
            # Call the initiate_data_ingestion method on the instance
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Got the data from URL")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise SignException(e, sys)

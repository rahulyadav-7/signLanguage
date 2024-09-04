import sys, os
from six.moves import urllib
import zipfile
from signLangugae.logger import logging
from signLangugae.exception import SignException
#from signLangugae.entity.config_entity import DataIngestionConfig
from signLangugae.entity.artifcats_entity import DataIngestionArtifact  # Ensure this import is correct


class DataIngestion:
    def __init__(self, data_ingestion_config):
        self.data_ingestion_config = data_ingestion_config
        
    def download_data(self) -> str:
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            
            data_file_name = os.path.basename(dataset_url).split('?')[0]  # Remove query parameters
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            
            logging.info(f"Downloading data from {dataset_url} into {zip_file_path}")
            urllib.request.urlretrieve(dataset_url, zip_file_path)
            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")
            
            return zip_file_path
        except Exception as e:
            raise SignException(e, sys)

    def extract_zip_file(self, zip_file_path: str) -> str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)
            
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
                
            logging.info(f'Extracted zip file: {zip_file_path} into dir: {feature_store_path}')
            return feature_store_path
        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e, sys)

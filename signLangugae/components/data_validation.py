import os
import sys
import shutil
from signLangugae.logger import logging
from signLangugae.exception import SignException
from signLangugae.entity.config_entity import DataValidationConfig
from signLangugae.entity.artifcats_entity import DataIngestionArtifact, DataValidationArtifact


class DataValidation:
    def __init__(
            self,
            data_ingestion_artifact: DataIngestionArtifact,
            data_validation_config: DataValidationConfig
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SignException(e, sys)

    def validate_all_files_exist(self) -> bool:
        try:
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            validation_status = all(file in all_files for file in self.data_validation_config.required_file_list)

            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validate_artifacts = DataValidationArtifact(validation_status=status)
            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data Validation artifact: {data_validate_artifacts}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validate_artifacts

        except Exception as e:
            raise SignException(e, sys)

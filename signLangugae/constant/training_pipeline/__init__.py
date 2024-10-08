import os

# Directory to store all artifacts
ARTIFACTS_DIR: str = "artifacts"

# Data Ingestion related constants
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://github.com/entbappy/Sign-Language-Generation-From-Video-using-YOLOV5/blob/master/Data/Sign_language_data.zip?raw=true"


# Data validation related constants
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_STATUS_FILE = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]


# Model trainer related constants
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NUMBER_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16


# Construct paths for the data ingestion process
DATA_INGESTION_DIR: str = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_DIR_NAME)
FEATURE_STORE_PATH: str = os.path.join(DATA_INGESTION_DIR, DATA_INGESTION_FEATURE_STORE_DIR)
ZIP_FILE_PATH: str = os.path.join(DATA_INGESTION_DIR, "Sign_language_data.zip")


# Example usage
if __name__ == "__main__":
    print("Artifacts Directory:", ARTIFACTS_DIR)
    print("Data Ingestion Directory:", DATA_INGESTION_DIR)
    print("Feature Store Path:", FEATURE_STORE_PATH)
    print("Zip File Path:", ZIP_FILE_PATH)
    print("Data Download URL:", DATA_DOWNLOAD_URL)

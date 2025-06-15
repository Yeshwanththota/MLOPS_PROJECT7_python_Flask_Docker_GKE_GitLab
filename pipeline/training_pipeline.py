from src.data_processing import DataProcessor
from src.model_training  import ModelTrainer

if __name__ == "__main__":
    data_processor = DataProcessor("artifacts/raw/data.csv")
    data_processor.run()

    trainer =  ModelTrainer()
    trainer.run()

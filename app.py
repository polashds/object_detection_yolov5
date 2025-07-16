# from wasteDetection.logger import logging
# from wasteDetection.exception import AppException
# import sys

#logging.info("Logger initialized successfully.")

# try:
#     a = 1 / 0
# except Exception as e:
#     raise AppException(e, sys)

from wasteDetection.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
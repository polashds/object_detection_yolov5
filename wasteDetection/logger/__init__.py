#create custom logger for waste detection project
import logging

import os
# track timestamp of log file
from datetime import datetime

from from_root import from_root

# Define the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the log directory if it doesn't exist
log_path = os.path.join(from_root(), 'log', LOG_FILE)

# create the directory if it does not exist
os.makedirs(log_path, exist_ok=True)

# Define the full path for the log file
lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# custom log format
logging.basicConfig(
    filename=lOG_FILE_PATH,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)
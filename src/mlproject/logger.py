import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # log file name with timestamp 
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)                # log file path          
os.makedirs(log_path,exist_ok=True)                               # create log directory if not exists

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)                 # log file path with name

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
import logging
from datetime import datetime
import os
import sys

to_day = datetime.now()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if getattr(sys, 'frozen', False):
    module_path = os.path.dirname(sys.executable)
elif __file__:
    module_path = os.path.dirname(__file__)
    

f_handler = logging.FileHandler(
    # os.path.dirname(__file__) + "/logFiles/emailFetch_{}_{}_{}.log".format(
    module_path + "/logFiles/emailFetch_{}_{}_{}.log".format(
        to_day.year, to_day.month, to_day.day),
    encoding="utf-8")
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
    ))

st_handler = logging.StreamHandler()
st_handler.setLevel(logging.DEBUG)
st_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
    ))

logger.addHandler(f_handler)
logger.addHandler(st_handler)
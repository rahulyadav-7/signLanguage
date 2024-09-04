from signLangugae.logger import logging
from signLangugae.exception import SignException
import sys

# try logging
logging.info("Welcome to the project")

# try exception
try:
    a = 7/'9'

except Exception as e:
    raise SignException(e, sys) from e
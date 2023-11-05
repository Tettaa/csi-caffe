import logging
import os

logging.config.fileConfig(os.environ['PYTHONPATH']+'/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)  

def caffelog() -> logging.Logger:
    return logging.getLogger(__name__)


class Caffelog:

    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)

    def log(self):
        return self.log
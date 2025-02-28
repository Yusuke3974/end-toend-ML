import sys
from security.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"{self.error_message} at line {self.lineno} in {self.filename}"

if __name__ == "__main__":
    try:
        logger.logging.info("This is a test message")
        a = 1/0
        print("This is a test message")
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
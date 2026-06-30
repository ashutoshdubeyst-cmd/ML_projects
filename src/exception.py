import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

# Your code defines a custom exception class that enhances error reporting by including the filename and line number where the error occurred. Let me break it down clearly:

# 🔍 How it works
# error_message_detail function

# Takes in the error and sys module.

# Extracts traceback info using error_detail.exc_info().

# Retrieves:

# Filename (exc_tb.tb_frame.f_code.co_filename)

# Line number (exc_tb.tb_lineno)

# Error message (str(error))

# Returns a formatted string with all these details.

# CustomException class

# Inherits from Python’s built-in Exception.

# Calls error_message_detail to generate a detailed error message.

# Overrides __str__ so printing the exception shows the detailed message.
'''
Logging is used for debugging in case of failures to find the root cause.
Method 1
1) Import Logging
2) Use basicConfig() method for filename, set the date/time, log level and message format
3) Create an logger object of logging class
4) set the log level(by default -Warning)
5) Using object print the log level message

Method 2
1) Import Logging
2) Use basicConfig() method for filename, set the date/time, log level and message format
3) set the log level(by default -Warning)
5) Using Logging method, print the log level message
'''

import logging

logging.basicConfig(filename="test.log",format='%(asctime)s: %(levelname)s: %(message)s',datefmt ='%m/%d/%y %I:%M:%S %p')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a Debug log")
logger.info("This is an Info log")
logger.warning("This is a Warning log")
logger.error("This is an Error log")
logger.critical("This is a Critical log")
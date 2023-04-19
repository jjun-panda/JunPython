import logging

logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format='%(levelname)s - %(asctime) - %(message)s')

logging.debug("Some messages")
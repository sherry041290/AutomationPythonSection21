import logging
logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s",
                    datefmt="%m-%d-%Y %I:%M:%S %p", level=logging.DEBUG)
logging.warning("This is warning!")
logging.error("this is error")
logging.info("Log information")

import logging


class LoggingConsole:
    def testLog(self):
        # Set name for log
        logger = logging.getLogger(LoggingConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create a handler
        handler1 = logging.StreamHandler()
        handler1.setLevel(logging.INFO)

        # Format for log
        format_log = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s : %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

        # Add format to the console
        handler1.setFormatter(format_log)

        # Add handle to the console log
        logger.addHandler(handler1)

        # message
        logger.warn("This is warning! ^^")
        logger.error("This is error")
        logger.info("Log information")
        logger.critical(" This is critical message")


testlog = LoggingConsole()
testlog.testLog()


import logging
import logging.config


class LoggingConfig:
    def testLog(self):
        # Set name for log
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggingConfig.__name__)

        # message
        logger.warn("This is warning! ^^")
        logger.error("This is error")
        logger.info("Log information")
        logger.critical(" This is critical message")


testlog = LoggingConfig()
testlog.testLog()


import logging
import loggingpackage.customlogger as cl


class demoCustomLogger:
    log = cl.customlogfile(logging.DEBUG)

    def demoMethod1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def demoMethod2(self):
        log_method2 = cl.customlogfile(logging.INFO)
        log_method2.debug('debug message')
        log_method2.info('info message')
        log_method2.warn('warn message')
        log_method2.error('error message')
        log_method2.critical('critical message')

    def demoMethod3(self):
        log_method3 = cl.customlogfile(logging.INFO)
        log_method3.debug('debug message')
        log_method3.info('info message')
        log_method3.warn('warn message')
        log_method3.error('error message')
        log_method3.critical('critical message')

test_log_method = demoCustomLogger()
test_log_method.demoMethod1()
test_log_method.demoMethod2()
test_log_method.demoMethod3()


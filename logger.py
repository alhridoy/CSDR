import datetime
import os

class Logger:
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    
    LEVELS = {0: 'DEBUG', 1: 'INFO', 2: 'WARNING', 3: 'ERROR', 4: 'CRITICAL'}
    
    def __init__(self, level=INFO, log_file=None):
        self.level = level
        self.log_file = log_file
    
    def _log(self, level, message):
        if level >= self.level:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"[{timestamp}] {self.LEVELS[level]}: {message}"
            print(log_entry)
            if self.log_file:
                with open(self.log_file, 'a') as f:
                    f.write(log_entry + '\n')
    
    def debug(self, message):
        self._log(self.DEBUG, message)
    
    def info(self, message):
        self._log(self.INFO, message)
    
    def warning(self, message):
        self._log(self.WARNING, message)
    
    def error(self, message):
        self._log(self.ERROR, message)
    
    def critical(self, message):
        self._log(self.CRITICAL, message)

# Example usage
if __name__ == '__main__':
    log = Logger(level=Logger.DEBUG, log_file='app.log')
    log.debug('Debug message')
    log.info('Info message')
    log.warning('Warning message')
    log.error('Error message')
    log.critical('Critical message')
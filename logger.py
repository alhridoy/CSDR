import sys
import datetime

class Logger:
    LEVELS = {'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}
    
    def __init__(self, name='Logger', level='INFO', log_file=None):
        self.name = name
        self.level = self.LEVELS[level]
        self.log_file = log_file
    
    def _log(self, level, message):
        if self.LEVELS[level] >= self.level:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"[{timestamp}] {level} - {self.name}: {message}"
            print(log_entry)
            if self.log_file:
                with open(self.log_file, 'a') as f:
                    f.write(log_entry + '\n')
    
    def debug(self, message):
        self._log('DEBUG', message)
    
    def info(self, message):
        self._log('INFO', message)
    
    def warning(self, message):
        self._log('WARNING', message)
    
    def error(self, message):
        self._log('ERROR', message)
    
    def critical(self, message):
        self._log('CRITICAL', message)

# Example usage
if __name__ == '__main__':
    log = Logger('TestApp', 'DEBUG', 'app.log')
    log.debug('Debug message')
    log.info('Info message')
    log.warning('Warning message')
    log.error('Error message')
    log.critical('Critical message')
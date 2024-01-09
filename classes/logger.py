import logging
import datetime
import os
import pathlib

LOG_PATH = f"./logs/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

def getCustomLogger(name, path="./logs/", level=logging.DEBUG):
    _log = logging.getLogger(name)
    _log.setLevel(level)
    _log.addHandler(getColoredConsole(level))
    _log.addHandler(getCustomFileHandler(path))
    return _log

def getCustomFileHandler(path="./logs/"):
    if not pathlib.Path(path).exists():
        os.makedirs(path)
    logsHandler = logging.FileHandler(LOG_PATH)
    logsHandler.setLevel(logging.INFO)
    logsHandler.encoding = "utf8"
    logsHandler.setFormatter(logging.Formatter(fmt=f'%(asctime)s %(levelname)-8s %(name)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    return logsHandler

def getColoredConsole(level = logging.DEBUG):
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(ColorFormatter())
    return ch

class ColorFormatter(logging.Formatter):
    LEVEL_COLORS = [
        (logging.DEBUG, '\x1b[40;1m'),
        (logging.INFO, '\x1b[34;1m'),
        (logging.WARNING, '\x1b[33;1m'),
        (logging.ERROR, '\x1b[31m'),
        (logging.CRITICAL, '\x1b[41m'),
    ]

    FORMATS = {
        level: logging.Formatter(
            f'\x1b[30;1m%(asctime)s\x1b[0m {color}%(levelname)-8s\x1b[0m \x1b[35m%(name)s\x1b[0m %(message)s',
            '%Y-%m-%d %H:%M:%S',
        )
        for level, color in LEVEL_COLORS
    }

    def format(self, record):
        formatter = self.FORMATS.get(record.levelno)
        if formatter is None:
            formatter = self.FORMATS[logging.DEBUG]

        if record.exc_info:
            text = formatter.formatException(record.exc_info)
            record.exc_text = f'\x1b[31m{text}\x1b[0m'

        output = formatter.format(record)
        record.exc_text = None
        return output
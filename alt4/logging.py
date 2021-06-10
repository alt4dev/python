import logging
from datetime import datetime
from alt4.writer import write_log
from alt4.settings import should_emmit
from alt4.grouping import close_group, open_group
from alt4.proto.definitions_pb2 import Log


class Logger:
    claims = {}
    call_depth = 3

    def __init__(self, **claims):
        self.claims = claims

    def _log(self, level, as_group, message, *args, **kwargs):
        try:
            message = str(message) % tuple(args)
            message = message.format(kwargs)
        except TypeError:
            pass  # Thrown if % format fails
        except KeyError:
            pass  # Thrown if format fails
        write_log(self.call_depth, as_group, message, self.claims, level, datetime.now())

    def warning(self, message, *args, **kwargs):
        if should_emmit():
            logging.warning(message)
        self._log(Log.Level.WARNING, False, message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        if should_emmit():
            logging.debug(message)
        self._log(Log.Level.DEBUG, False, message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        if should_emmit():
            logging.error(message)
        self._log(Log.Level.ERROR, False, message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        if should_emmit():
            logging.info(message)
        self._log(Log.Level.INFO, False, message, *args, **kwargs)

    def fatal(self, message, *args, **kwargs):
        if should_emmit():
            logging.fatal(message)
        self._log(Log.Level.INFO, False, message, *args, **kwargs)

    def open_group(self, message, *args, **kwargs):
        open_group()
        if should_emmit():
            logging.info(message)
        self._log(Log.Level.NONE, True, message, *args, **kwargs)

    def close_group(self, *args, **kwargs):
        if args:
            message = args[0]
            args = args[1:]
            if should_emmit():
                logging.info(message)
            self._log(Log.Level.NONE, True, message, *args, **kwargs)
        close_group()

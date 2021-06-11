import logging
from datetime import datetime
from alt4.writer import write_log
from alt4.settings import should_emmit
from alt4.grouping import close_group as native_close, open_group as native_open
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
        native_open()
        if should_emmit():
            logging.info(message)
        self._log(Log.Level.NONE, True, message, *args, **kwargs)

    def close_group(self, *args, **kwargs):
        if args:
            message = str(args[0])
            args = args[1:]
            if should_emmit():
                logging.info(message)
            self._log(Log.Level.NONE, True, message, *args, **kwargs)
        native_close()


global __default_logger


def get_default_logger():
    global __default_logger
    if "__default_logger" in globals():
        return __default_logger
    __default_logger = Logger()
    __default_logger.call_depth += 1
    return __default_logger


def warning(message, *args, **kwargs):
    get_default_logger().warning(message, *args, **kwargs)


def debug(message, *args, **kwargs):
    get_default_logger().debug(message, *args, **kwargs)


def info(message, *args, **kwargs):
    get_default_logger().info(message, *args, **kwargs)


def error(message, *args, **kwargs):
    get_default_logger().error(message, *args, **kwargs)


def fatal(message, *args, **kwargs):
    get_default_logger().fatal(message, *args, **kwargs)


def open_group(message, *args, **kwargs):
    get_default_logger().open_group(message, *args, **kwargs)


def close_group(*args, **kwargs):
    get_default_logger().close_group(*args, **kwargs)


import os
from alt4.exceptions import MissingTokenException
global MODE
global SOURCE
global AUTH_TOKEN


MODE_RELEASE = "release"
MODE_DEBUG = "debug"
MODE_TESTING = "testing"
MODE_SILENT = "silent"


def set_mode(mode=None):
    if not mode:
        # Get the mode from environment variable
        mode = os.environ.get("ALT4_MODE", MODE_RELEASE)
    if mode in [MODE_RELEASE, MODE_TESTING, MODE_DEBUG, MODE_SILENT]:
        global MODE
        MODE = mode


def get_mode():
    global MODE
    if "MODE" in globals():
        return MODE
    set_mode()
    return get_mode()


def should_emmit():
    mode = get_mode()
    return mode == MODE_DEBUG or mode == MODE_TESTING


def skip_remote():
    mode = get_mode()
    return mode == MODE_TESTING or mode == MODE_SILENT


def set_source(source=None):
    if not source:
        # Get the mode from environment variable
        source = os.environ.get("ALT4_SOURCE", "default")
    global SOURCE
    SOURCE = source


def get_source():
    global SOURCE
    if "SOURCE" in globals():
        return SOURCE
    set_source()
    return get_source()


def set_auth_token(auth_token=None):
    if not auth_token:
        # Get the mode from environment variable
        auth_token = os.environ.get("ALT4_AUTH_TOKEN", None)
    if not auth_token:
        raise MissingTokenException("Invalid auth token provided")
    global AUTH_TOKEN
    AUTH_TOKEN = auth_token


def get_auth_token():
    global AUTH_TOKEN
    if "AUTH_TOKEN" in globals():
        return AUTH_TOKEN
    set_auth_token()
    return get_auth_token()

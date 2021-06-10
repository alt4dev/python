import uuid
import logging

global GROUP_ID


def open_group():
    global GROUP_ID
    if "GROUP_ID" in globals():
        logging.warning("ALT4WARNING: Unclosed group found, make sure to call close_group() after open_group()")
    GROUP_ID = uuid.uuid4().hex


def close_group():
    global GROUP_ID
    if "GROUP_ID" in globals():
        del GROUP_ID


def get_group():
    global GROUP_ID
    if "GROUP_ID" in globals():
        return GROUP_ID
    return ""

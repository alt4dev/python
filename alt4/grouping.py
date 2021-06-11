import uuid
import logging
import threading

global GROUP_ID
global WAIT_GROUP


def open_group():
    global GROUP_ID
    global WAIT_GROUP
    if "GROUP_ID" in globals():
        logging.warning("ALT4WARNING: Unclosed group found, make sure to call close_group() after open_group()")
    GROUP_ID = uuid.uuid4().hex
    WAIT_GROUP = WaitGroup()


def close_group():
    global WAIT_GROUP
    global GROUP_ID
    if "GROUP_ID" in globals():
        del GROUP_ID
    if "WAIT_GROUP" in globals():
        # Wait for the group to finish writing
        WAIT_GROUP.wait()
        del WAIT_GROUP


def get_group():
    if "GROUP_ID" in globals():
        return GROUP_ID, WAIT_GROUP
    return "", WaitGroup()


# Credit: https://gist.github.com/pteichman/84b92ae7cef0ab98f5a8
class WaitGroup(object):
    """WaitGroup is like Go sync.WaitGroup.

    Without all the useful corner cases.
    """

    def __init__(self):
        self.count = 0
        self.cv = threading.Condition()

    def add(self, n):
        self.cv.acquire()
        self.count += n
        self.cv.release()

    def done(self):
        self.cv.acquire()
        self.count -= 1
        if self.count == 0:
            self.cv.notify_all()
        self.cv.release()

    def wait(self):
        self.cv.acquire()
        while self.count > 0:
            self.cv.wait()
        self.cv.release()

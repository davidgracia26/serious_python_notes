import os

from unittest import mock


def fake_os_unlink(path):
    raise IOError("Testing")


with mock.patch('os.unlink', fake_os_unlink):
    os.unlink('foobar')
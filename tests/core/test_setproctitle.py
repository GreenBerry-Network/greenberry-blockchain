import unittest

from greenberry.util.setproctitle import setproctitle


class TestSetProcTitle(unittest.TestCase):
    def test_does_not_crash(self):
        setproctitle("greenberry test title")

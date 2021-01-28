import unittest

from tests.dataset_loading import TestDatasetLoading
from tests.callbacks import TestCallbacks


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDatasetLoading('test_all'))
    suite.addTest(TestCallbacks('test_all'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

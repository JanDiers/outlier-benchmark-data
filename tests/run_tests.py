import unittest

from tests.dataset_loading import TestDatasetLoading as Dataset
from tests.test_dataset_collection import TestDatasetCollection as Collection
from tests.test_documentation import TestDocumentation as Documentation


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Dataset('test_all'))
    suite.addTest(Documentation('test_all'))
    suite.addTest(Collection('test_all'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

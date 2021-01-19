import unittest


class AllDatasets(unittest.TestCase):
    from outlier_benchmark.datasets import wbc
    ls = [wbc]


import importlib
import inspect
import shutil
import unittest
import re
from pathlib import Path

import numpy as np
import pandas as pd

from outlier_benchmark.datasets import __all__ as all_datasets
from outlier_benchmark.datasets.base.dataset import BaseDataset


class TestDocumentation(unittest.TestCase):

    def setUp(self) -> None:
        self.datasets = []

        module = importlib.import_module('outlier_benchmark.datasets')

        for ds in all_datasets:
            dataset = getattr(module, ds)
            if inspect.isclass(dataset):
                dataset = dataset()

            self.datasets.append(dataset)

    def test_all(self):
        self.test_specification_table()
        self.test_doctests()

    def test_specification_table(self):
        all_specifications = [
            ('num_samples', 'number of samples:'),
            ('num_features', 'number of features:'),
            ('num_outlier', 'number of outliers:'),
            ('pct_outlier', 'percentage outliers:'),
            ('num_duplicates', 'number of duplicates:'),
        ]

        for dataset in self.datasets:
            for attr, specification in all_specifications:
                pattern = rf'{specification}[ |]+([\d\.]+)'
                found = re.findall(pattern, dataset.__doc__, re.MULTILINE)
                if len(found) > 1:
                    raise ValueError(f'Expected 1 found, but got: {found}')
                found = float(found[0])
                expected = dataset.__getattribute__(attr)
                self.assertTrue(np.allclose(expected, found), f'{dataset.name}: {specification} in docs: {found}, but '
                                                              f'correct is: {expected}.')

    def test_doctests(self):
        import doctest
        for p in Path('../outlier_benchmark').glob('**/*.py'):
            doctest.testfile(str(p))

import importlib
import inspect
import unittest
from dataclasses import field, dataclass

from outlier_benchmark.data_collection import DatasetCollection
from outlier_benchmark.datasets import __all__ as all_datasets
from outlier_benchmark.datasets.base import BaseDataset


class TestDatasetCollection(unittest.TestCase):

    def test_all(self):
        self.test_all_datasets_included()
        self.test_custom_datasets_included()
        self.test_filter()

    def test_all_datasets_included(self):
        collection = DatasetCollection()

        module = importlib.import_module('outlier_benchmark.datasets')

        for dataset in all_datasets:

            dataset = getattr(module, dataset)

            if inspect.isclass(dataset):
                dataset = dataset()

            self.assertTrue(dataset in collection, f'{dataset.name} is not included in DatasetCollection.')

    def test_custom_datasets_included(self):
        @dataclass
        class MyNewDataset(BaseDataset):
            name: str = field(default='MyNewDataset', init=False)
            num_samples: int = field(default=444, init=False)
            num_features: int = field(default=333, init=False)
            num_outlier: int = field(default=222, init=False)
            num_duplicates: int = field(default=111, init=False)

        collection = DatasetCollection()
        self.assertIn(MyNewDataset(), collection)
        self.assertTrue(MyNewDataset() == collection[-1])

    def test_filter(self):
        m, x = 1, 455
        ds = DatasetCollection().num_samples(minimum=m, maximum=x)
        for dataset in ds:
            self.assertTrue(m <= dataset.num_samples <= x,
                            f'num_samples filter failed: dataset has {dataset.num_samples} samples.')
            self.assertIn('num_samples', ds.filters_applied, f'num_samples not in filters_applied')

        m, x = 5, 20
        ds = DatasetCollection().num_features(minimum=m, maximum=x)
        for dataset in ds:
            self.assertTrue(m <= dataset.num_features <= x,
                            f'num_samples filter failed: dataset has {dataset.num_features} features.')
            self.assertIn('num_features', ds.filters_applied, f'num_features not in filters_applied')

        m, x = 5, 12
        ds = DatasetCollection().num_outlier(minimum=m, maximum=x)
        for dataset in ds:
            self.assertTrue(m <= dataset.num_outlier <= x,
                            f'num_samples filter failed: dataset has {dataset.num_outlier} outliers.')
            self.assertIn('num_outlier', ds.filters_applied, f'num_outlier not in filters_applied')

        m, x = 8, float('inf')
        ds = DatasetCollection().num_duplicates(minimum=m)
        for dataset in ds:
            self.assertTrue(m <= dataset.num_duplicates <= x,
                            f'num_duplicates filter failed: dataset has {dataset.num_duplicates} duplicates.')
            self.assertIn('num_duplicates', ds.filters_applied, f'num_duplicates not in filters_applied')

        m, x = 0, 40
        ds = DatasetCollection().pct_outlier(maximum=x)
        for dataset in ds:
            self.assertTrue(m <= dataset.pct_outlier <= x,
                            f'pct_outlier filter failed: dataset has {dataset.pct_outlier} pct_outlier.')
            self.assertIn('pct_outlier', ds.filters_applied, f'pct_outlier not in filters_applied')

        fun = lambda d: 'A' in d.name
        ds = DatasetCollection().LambdaFilter(fun)
        for dataset in ds:
            self.assertTrue('A' in dataset.name,
                            f'LambdaFilter filter failed: dataset has datasets without "A"')
            self.assertIn('<lambda>', ds.filters_applied, f'lambda not in filters_applied')

import importlib
import inspect
import shutil
import unittest

import numpy as np
import pandas as pd

from outlier_benchmark.datasets import __all__ as all_datasets
from outlier_benchmark.datasets.base.dataset import BaseDataset


class TestDatasetLoading(unittest.TestCase):

    def test_all(self):
        self.test_download_and_loading()
        self.test_no_parameters_allowed_in_dataset_classes()
        self.test_all_importable()
        self.test_instance_attributes()

    def test_instance_attributes(self):
        module = importlib.import_module('outlier_benchmark.datasets')
        for ds in all_datasets:
            dataset = getattr(module, ds)
            if inspect.isclass(dataset):
                dataset = dataset()

            dataset: BaseDataset
            X, y = dataset.load()

            print(f'Check attributes for {dataset.name}')

            # check name
            self.assertTrue(dataset.name.lower() == ds.lower(),
                            f'names do not match: {dataset.name.lower()} != {ds.lower()}')

            self.assertTrue(dataset.num_samples == X.shape[0],
                            f'num_samples do not match: {dataset.num_samples} != {X.shape[0]}')

            self.assertTrue(dataset.num_features == X.shape[1],
                            f'num_features do not match: {dataset.num_features} != {X.shape[1]}')

            self.assertTrue(dataset.num_outlier == y.sum(),
                            f'num_outlier do not match: {dataset.num_outlier} != {y.sum()}')

            df = pd.DataFrame(X)
            df['outlier'] = y
            duplicated = df.duplicated().sum()
            self.assertTrue(dataset.num_duplicates == duplicated,
                            f'num_duplicates do not match: {dataset.num_duplicates} != {duplicated}')

            outlier_pct = round(y.sum() / X.shape[0], 4) * 100
            self.assertTrue(np.isclose(dataset.pct_outlier, outlier_pct),
                            f'pct_outlier do not match: {dataset.pct_outlier} != {outlier_pct}')

    def test_all_importable(self):
        for dataset in all_datasets:
            print('try to import', dataset)
            exec(f'from outlier_benchmark.datasets import {dataset} as dataset')

    def test_download_and_loading(self):
        module = importlib.import_module('outlier_benchmark.datasets')

        for dataset in all_datasets:

            dataset = getattr(module, dataset)

            if inspect.isclass(dataset):
                dataset = dataset()

            print(f'dataset {dataset.name} - try download with download=False')
            path = dataset.path

            # remove previously downloaded file
            if path.exists():
                shutil.rmtree(path.parent)

            # assert no download is triggered if download = False
            with self.assertRaises(ValueError):
                dataset.load(download=False)

            print(f'dataset {dataset.name} - try download from github')

            X, y = dataset.load(download=True)

            self.assertTrue(isinstance(X, np.ndarray))
            self.assertTrue(isinstance(y, np.ndarray))

    def test_no_parameters_allowed_in_dataset_classes(self):
        module = importlib.import_module('outlier_benchmark.datasets')

        for dataset in all_datasets:

            dataset = getattr(module, dataset)

            if inspect.isclass(dataset):
                print('Ensure no parameters are allowed for instantiating datasets')
                with self.assertRaises(TypeError):
                    dataset(5)
                    dataset(name='not_allowed_to_pass_names')

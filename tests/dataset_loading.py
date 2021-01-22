import importlib
import inspect
import shutil
import unittest

import numpy as np

from outlier_benchmark.datasets import __all__ as all_datasets


class TestDatasetLoading(unittest.TestCase):

    def test_all(self):
        self.test_download_and_loading()
        self.test_no_parameters_allowed_in_dataset_classes()
        self.test_all_importable()

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


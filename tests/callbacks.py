import importlib
import inspect
import unittest

import numpy as np

from outlier_benchmark.callbacks.normalize import NormalizeCallback
from outlier_benchmark.datasets import __all__ as all_datasets


class TestCallbacks(unittest.TestCase):

    def setUp(self) -> None:
        module = importlib.import_module('outlier_benchmark.datasets')
        datasets = [getattr(module, dataset) for dataset in all_datasets]
        self.datasets = [dataset() if inspect.isclass(dataset) else dataset for dataset in datasets]

    def test_all(self):
        self.test_normalize()
        self.test_normalize_method_in_datasets()

    def test_normalize_method_in_datasets(self):
        from sklearn.preprocessing import minmax_scale

        for dataset in self.datasets:

            print(f'Ensure {dataset}.normalize().load() works as expected')

            dataset.remove_callbacks()

            X, _ = dataset.load()

            expected_X = minmax_scale(X, feature_range=(0, 1))

            X, _ = dataset.normalize().load()

            self.assertTrue(np.allclose(X, expected_X),
                            f'{dataset.name}: does not match scaling according to scikit-learn. '
                            f'\n received:\n {X} \n expected: \n {expected_X}')

    def test_normalize(self):

        from sklearn.preprocessing import minmax_scale

        for dataset in self.datasets:
            print(f'{dataset}: Ensure NormalizeCallback(minimum=0, maximum=1) works as expected')

            dataset.remove_callbacks()
            X, _ = dataset.load()
            expected_X = minmax_scale(X, feature_range=(0, 1))

            dataset.add_callback(NormalizeCallback(minimum=0, maximum=1))
            X, _ = dataset.load()

            self.assertTrue(np.allclose(X, expected_X),
                            f'{dataset.name}: does not match scaling according to scikit-learn. '
                            f'\n received:\n {X} \n expected: \n {expected_X}')

            print(f'{dataset}: Ensure NormalizeCallback(minimum=-0.3, maximum=55) works as expected')

            expected_X = minmax_scale(X, feature_range=(-0.3, 55))
            dataset.add_callback(NormalizeCallback(minimum=-0.3, maximum=55))

            X, _ = dataset.load()

            self.assertTrue(np.allclose(X, expected_X),
                            f'{dataset.name}: does not match scaling according to scikit-learn. '
                            f'\n received:\n {X} \n expected: \n {expected_X}')

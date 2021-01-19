import shutil
import unittest
from pathlib import Path

import numpy as np

from outlier_benchmark.datasets import __all__ as all_datasets


class TestStringMethods(unittest.TestCase):

    def test_all_importable(self):
        dataset_names = [dataset.name for dataset in all_datasets]
        for path in Path('../outlier_benchmark/datasets/').iterdir():
            folder_name = path.stem
            if folder_name[0] == '_' and folder_name[1] != '_':
                self.assertIn(folder_name[1:], dataset_names)

    def test_download_and_loading(self):
        from outlier_benchmark.datasets import __all__ as all_datasets
        for dataset in all_datasets:
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


if __name__ == '__main__':
    unittest.main()

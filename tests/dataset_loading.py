import unittest
import shutil

import numpy as np


class TestStringMethods(unittest.TestCase):

    def test_download(self):
        from outlier_benchmark.datasets import wbc
        path = wbc.path

        # remove previously downloaded file
        if path.exists():
            shutil.rmtree(path.parent)

        # assert no download is triggered if download = False
        with self.assertRaises(ValueError):
            wbc.load(download=False)

        X, y = wbc.load(download=True)

        self.assertTrue(isinstance(X, np.ndarray))
        self.assertTrue(isinstance(y, np.ndarray))


if __name__ == '__main__':
    unittest.main()

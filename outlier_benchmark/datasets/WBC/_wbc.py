from typing import Tuple

import numpy as np
import pandas as pd

from outlier_benchmark.datasets.base.dataset import BaseDataset


class WBC(BaseDataset):
    """
    The WBC dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   454  |
    +-----------------------+--------+
    |number of features:    |   9    |
    +-----------------------+--------+
    |number of outliers:    |   10   |
    +-----------------------+--------+
    |percentage outliers:   |   2.2 %|
    +-----------------------+--------+
    |number of duplicates:  |   231  |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. When you call wbc.load(), the data is not normalized and contains
    duplicates.

    Usage:

    >>> from outlier_benchmark.datasets import wbc
    >>> X, y = wbc.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (454, 9)
    >>> y.sum()  # 10, meaning 10 outliers in the dataset
    >>> X.max()  # 10.0
    >>> X.min()  # 1.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenková, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    def load(self, download: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        """
        loads the data X and y, both numpy arrays. If not previously downloaded and download = True, before loading
        the dataset will be downloaded to your local machine.

        Example:
        >>> from outlier_benchmark.datasets import wbc
        >>> X, y = wbc.load(download=True)  # download will only take place if not previously downloaded
        >>> X.shape  # (454, 9)

        :param download: bool, if download is allowed
        :return: X and y, both numpy arrays.
        """
        if not self.path.exists():
            if download:
                super(WBC, self).download()
            else:
                raise ValueError(f'wbc has not yet been downloaded to your machine and you set download=False.'
                                 f'set download=True to download and load data.')

        df = pd.read_csv(self.path)
        X = df.drop('outlier', axis=1).values
        y = df['outlier'].values
        return X, y

    name: str = 'WBC'
    num_samples: int = 155
    num_features: int = 10
    num_outlier: int = 5

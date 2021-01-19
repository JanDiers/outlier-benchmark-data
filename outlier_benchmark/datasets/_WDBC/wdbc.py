from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class WDBC(BaseDataset):
    """
    The WDBC dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   367  |
    +-----------------------+--------+
    |number of features:    |   30   |
    +-----------------------+--------+
    |number of outliers:    |   10   |
    +-----------------------+--------+
    |percentage outliers:   | 2.72 % |
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/WDBC/WDBC_withoutdupl_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import wdbc
    >>> X, y = wdbc.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (367, 30)
    >>> y.sum()  # 10, the number of outliers in the dataset
    >>> X.max()  # 3234.0
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'WDBC'
    num_samples: int = 367
    num_features: int = 30
    num_outlier: int = 10
    number_duplicates: int = 0

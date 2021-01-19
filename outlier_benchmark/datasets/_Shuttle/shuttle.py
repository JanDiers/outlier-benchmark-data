from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Shuttle(BaseDataset):
    """
    The Shuttle dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   1013 |
    +-----------------------+--------+
    |number of features:    |   9    |
    +-----------------------+--------+
    |number of outliers:    |   13   |
    +-----------------------+--------+
    |percentage outliers:   |  1.28 %|
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/Shuttle/Shuttle_withoutdupl_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import shuttle
    >>> X, y = shuttle.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (1013, 9)
    >>> y.sum()  # 13, the number of outliers in the dataset
    >>> X.max()  # 15164.0
    >>> X.min()  # -1471.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'Shuttle'
    num_samples: int = 1013
    num_features: int = 9
    num_outlier: int = 13
    number_duplicates: int = 0

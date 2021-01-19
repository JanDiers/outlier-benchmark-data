from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Wilt(BaseDataset):
    """
    The Wilt dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |  4839  |
    +-----------------------+--------+
    |number of features:    |   5    |
    +-----------------------+--------+
    |number of outliers:    |  261   |
    +-----------------------+--------+
    |percentage outliers:   |  5.39 %|
    +-----------------------+--------+
    |number of duplicates:  |   20   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/Wilt/Wilt_05.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import wilt
    >>> X, y = wilt.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (4839, 5)
    >>> y.sum()  # 261, the number of outliers in the dataset
    >>> X.max()  # 1848.916667
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'Wilt'
    num_samples: int = 4839
    num_features: int = 5
    num_outlier: int = 261
    number_duplicates: int = 20

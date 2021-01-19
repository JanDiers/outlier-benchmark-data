from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class KDDCup99(BaseDataset):
    """
    The KDDCup99 dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |  60839 |
    +-----------------------+--------+
    |number of features:    |   41   |
    +-----------------------+--------+
    |number of outliers:    |   246  |
    +-----------------------+--------+
    |percentage outliers:   |   0.4 %|
    +-----------------------+--------+
    |number of duplicates:  |  12726 |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/KDDCup99/KDDCup99_idf.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import kddcup99
    >>> X, y = kddcup99.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (60839, 41)
    >>> y.sum()  # 246, the number of outliers in the dataset
    >>> X.max()  # 6291668.0
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'KDDCup99'
    num_samples: int = 60839
    num_features: int = 41
    num_outlier: int = 246
    number_duplicates: int = 12726

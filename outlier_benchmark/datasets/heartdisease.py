from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class HeartDisease(BaseDataset):
    """
    The HeartDisease dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   157  |
    +-----------------------+--------+
    |number of features:    |   13   |
    +-----------------------+--------+
    |number of outliers:    |    7   |
    +-----------------------+--------+
    |percentage outliers:   |  4.46 %|
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/HeartDisease/HeartDisease_withoutdupl_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import heartdisease
    >>> X, y = heartdisease.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (157, 13)
    >>> y.sum()  # 7, the number of outliers in the dataset
    >>> X.max()  # 564.0
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = field(default='HeartDisease', init=False)
    num_samples: int = field(default=157, init=False)
    num_features: int = field(default=13, init=False)
    num_outlier: int = field(default=7, init=False)
    number_duplicates: int = field(default=0, init=False)


heartdisease = HeartDisease()

from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Arrhythmia(BaseDataset):
    """
    The Arrhythmia dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   256  |
    +-----------------------+--------+
    |number of features:    |   259  |
    +-----------------------+--------+
    |number of outliers:    |   12   |
    +-----------------------+--------+
    |percentage outliers:   |  4.69 %|
    +-----------------------+--------+
    |number of duplicates:  |   0    |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/Arrhythmia/Arrhythmia_withoutdupl_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import arrhythmia
    >>> X, y = arrhythmia.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (256, 259)
    >>> y.sum()  # 12, the number of outliers in the dataset
    >>> X.max()  # 524.0
    >>> X.min()  # -112.1

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'Arrhythmia'
    num_samples: int = 256
    num_features: int = 259
    num_outlier: int = 12
    number_duplicates: int = 0

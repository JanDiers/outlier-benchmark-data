from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Hepatitis(BaseDataset):
    """
    The Hepatitis dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |    70  |
    +-----------------------+--------+
    |number of features:    |   19   |
    +-----------------------+--------+
    |number of outliers:    |    3   |
    +-----------------------+--------+
    |percentage outliers:   |  4.29 %|
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/Hepatitis/Hepatitis_withoutdupl_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import hepatitis
    >>> X, y = hepatitis.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (70, 19)
    >>> y.sum()  # 3, the number of outliers in the dataset
    >>> X.max()  # 420.0
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'Hepatitis'
    num_samples: int = 70
    num_features: int = 19
    num_outlier: int = 3
    number_duplicates: int = 0

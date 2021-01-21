from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Glass(BaseDataset):
    """
    The Glass dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   214  |
    +-----------------------+--------+
    |number of features:    |    7   |
    +-----------------------+--------+
    |number of outliers:    |    9   |
    +-----------------------+--------+
    |percentage outliers:   |  4.21 %|
    +-----------------------+--------+
    |number of duplicates:  |    1   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/Glass/Glass_withoutdupl_norm.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import glass
    >>> X, y = glass.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (214, 7)
    >>> y.sum()  # 9, the number of outliers in the dataset
    >>> X.max()  # 1.0
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = field(default='Glass', init=False)
    num_samples: int = field(default=214, init=False)
    num_features: int = field(default=7, init=False)
    num_outlier: int = field(default=9, init=False)
    num_duplicates: int = field(default=1, init=False)


glass = Glass()

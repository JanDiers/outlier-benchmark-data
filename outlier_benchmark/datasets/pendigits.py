from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class PenDigits(BaseDataset):
    """
    The PenDigits dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   9868 |
    +-----------------------+--------+
    |number of features:    |   16   |
    +-----------------------+--------+
    |number of outliers:    |   20   |
    +-----------------------+--------+
    |percentage outliers:   |  0.2 % |
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/PenDigits/PenDigits_withoutdupl_norm_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import pendigits
    >>> X, y = pendigits.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (9868, 16)
    >>> y.sum()  # the number of outliers in the dataset
    20
    >>> X.max()
    100.0
    >>> X.min()
    0.0

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
        datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016).
        https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='PenDigits', init=False)
    num_samples: int = field(default=9868, init=False)
    num_features: int = field(default=16, init=False)
    num_outlier: int = field(default=20, init=False)
    num_duplicates: int = field(default=0, init=False)


pendigits = PenDigits()

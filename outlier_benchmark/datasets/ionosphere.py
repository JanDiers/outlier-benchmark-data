from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Ionosphere(BaseDataset):
    """
    The Ionosphere dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   351  |
    +-----------------------+--------+
    |number of features:    |   32   |
    +-----------------------+--------+
    |number of outliers:    |  126   |
    +-----------------------+--------+
    |percentage outliers:   |  35.9 %|
    +-----------------------+--------+
    |number of duplicates:  |    1   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/Ionosphere/Ionosphere_withoutdupl_norm.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import ionosphere
    >>> X, y = ionosphere.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (351, 32)
    >>> y.sum()  # 126, the number of outliers in the dataset
    >>> X.max()  # 1.0
    >>> X.min()  # 0.0

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
        datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016).
        https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='Ionosphere', init=False)
    num_samples: int = field(default=351, init=False)
    num_features: int = field(default=32, init=False)
    num_outlier: int = field(default=126, init=False)
    num_duplicates: int = field(default=1, init=False)


ionosphere = Ionosphere()

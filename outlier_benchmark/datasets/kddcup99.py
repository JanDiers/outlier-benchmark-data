from dataclasses import dataclass, field

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
    >>> X.shape
    (60839, 41)
    >>> y.sum()
    246
    >>> X.max()
    6291668.0
    >>> X.min()
    0.0

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
        datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016).
        https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='KDDCup99', init=False)
    num_samples: int = field(default=60839, init=False)
    num_features: int = field(default=41, init=False)
    num_outlier: int = field(default=246, init=False)
    num_duplicates: int = field(default=12726, init=False)


kddcup99 = KDDCup99()

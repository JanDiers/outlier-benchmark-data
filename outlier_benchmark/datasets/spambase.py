from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class SpamBase(BaseDataset):
    """
    The SpamBase dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |  2934  |
    +-----------------------+--------+
    |number of features:    |  57    |
    +-----------------------+--------+
    |number of outliers:    |  146   |
    +-----------------------+--------+
    |percentage outliers:   |  4.98 %|
    +-----------------------+--------+
    |number of duplicates:  |   261  |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/SpamBase/SpamBase_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import spambase
    >>> X, y = spambase.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (2934, 57)
    >>> y.sum()  # 146, the number of outliers in the dataset
    >>> X.max()  # 9088.0
    >>> X.min()  # 0.0

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
        datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016).
        https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='SpamBase', init=False)
    num_samples: int = field(default=2934, init=False)
    num_features: int = field(default=57, init=False)
    num_outlier: int = field(default=146, init=False)
    num_duplicates: int = field(default=261, init=False)


spambase = SpamBase()

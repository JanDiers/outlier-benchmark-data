from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class WBC(BaseDataset):
    """
    The WBC dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   454  |
    +-----------------------+--------+
    |number of features:    |   9    |
    +-----------------------+--------+
    |number of outliers:    |   10   |
    +-----------------------+--------+
    |percentage outliers:   |   2.2 %|
    +-----------------------+--------+
    |number of duplicates:  |   231  |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/WBC/WBC_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import wbc
    >>> X, y = wbc.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (454, 9)
    >>> y.sum()  # 10, the number of outliers in the dataset
    >>> X.max()  # 10.0
    >>> X.min()  # 1.0

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
    datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016). https://doi.org/10.1007/s10618-015-0444-8
10
    """

    name: str = field(default='WBC', init=False)
    num_samples: int = field(default=454, init=False)
    num_features: int = field(default=9, init=False)
    num_outlier: int = field(default=10, init=False)
    num_duplicates: int = field(default=231, init=False)


wbc = WBC()

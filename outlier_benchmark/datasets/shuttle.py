from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Shuttle(BaseDataset):
    """
    The Shuttle dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   1013 |
    +-----------------------+--------+
    |number of features:    |   9    |
    +-----------------------+--------+
    |number of outliers:    |   13   |
    +-----------------------+--------+
    |percentage outliers:   |  1.28 %|
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/Shuttle/Shuttle_withoutdupl_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import shuttle
    >>> X, y = shuttle.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (1013, 9)
    >>> y.sum()  # 13, the number of outliers in the dataset
    >>> X.max()  # 15164.0
    >>> X.min()  # -1471.0

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
    datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016). https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='Shuttle', init=False)
    num_samples: int = field(default=1013, init=False)
    num_features: int = field(default=9, init=False)
    num_outlier: int = field(default=13, init=False)
    num_duplicates: int = field(default=0, init=False)


shuttle = Shuttle()

from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class PageBlocks(BaseDataset):
    """
    The PageBlocks dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |  5171  |
    +-----------------------+--------+
    |number of features:    |   10   |
    +-----------------------+--------+
    |number of outliers:    |  258   |
    +-----------------------+--------+
    |percentage outliers:   |  4.99 %|
    +-----------------------+--------+
    |number of duplicates:  |    37  |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/PageBlocks/PageBlocks_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import pageblocks
    >>> X, y = pageblocks.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (5171, 10)
    >>> y.sum()  # the number of outliers in the dataset
    258
    >>> X.max()
    143993.0
    >>> X.min()
    0.012

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
        datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016).
        https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='PageBlocks', init=False)
    num_samples: int = field(default=5171, init=False)
    num_features: int = field(default=10, init=False)
    num_outlier: int = field(default=258, init=False)
    num_duplicates: int = field(default=37, init=False)


pageblocks = PageBlocks()

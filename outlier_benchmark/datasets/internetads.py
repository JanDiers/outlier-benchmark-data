from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class InternetAds(BaseDataset):
    """
    The InternetAds dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |  2957  |
    +-----------------------+--------+
    |number of features:    |  1555  |
    +-----------------------+--------+
    |number of outliers:    |  147   |
    +-----------------------+--------+
    |percentage outliers:   |  4.97 %|
    +-----------------------+--------+
    |number of duplicates:  |  1219  |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/InternetAds/InternetAds_norm_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import internetads
    >>> X, y = internetads.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (2957, 1555)
    >>> y.sum()  # 147, the number of outliers in the dataset
    >>> X.max()  # 1.0
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = field(default='InternetAds', init=False)
    num_samples: int = field(default=2957, init=False)
    num_features: int = field(default=1555, init=False)
    num_outlier: int = field(default=147, init=False)
    num_duplicates: int = field(default=1219, init=False)


internetads = InternetAds()

from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Lymphography(BaseDataset):
    """
    The Lymphography dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   148  |
    +-----------------------+--------+
    |number of features:    |   18   |
    +-----------------------+--------+
    |number of outliers:    |    6   |
    +-----------------------+--------+
    |percentage outliers:   |  4.05 %|
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/Lymphography/Lymphography_withoutdupl_idf.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import lymphography
    >>> X, y = lymphography.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (148, 18)
    >>> y.sum()  # 6, the number of outliers in the dataset
    >>> X.max()  # 8.0
    >>> X.min()  # 0.0484523833859467

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = field(default='Lymphography', init=False)
    num_samples: int = field(default=148, init=False)
    num_features: int = field(default=18, init=False)
    num_outlier: int = field(default=6, init=False)
    num_duplicates: int = field(default=0, init=False)


lymphography = Lymphography()

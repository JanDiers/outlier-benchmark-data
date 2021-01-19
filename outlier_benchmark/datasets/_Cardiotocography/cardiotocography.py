from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cardiotocography(BaseDataset):
    """
    The Cardiotocography dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |   1742 |
    +-----------------------+--------+
    |number of features:    |   21   |
    +-----------------------+--------+
    |number of outliers:    |   87   |
    +-----------------------+--------+
    |percentage outliers:   |  4.99 %|
    +-----------------------+--------+
    |number of duplicates:  |   9    |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/Cardiotocography/Cardiotocography_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import cardiotocography
    >>> X, y = cardiotocography.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (1742, 21)
    >>> y.sum()  # 87, the number of outliers in the dataset
    >>> X.max()  # 564.0
    >>> X.min()  # -1.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'Cardiotocography'
    num_samples: int = 1742
    num_features: int = 21
    num_outlier: int = 87
    number_duplicates: int = 9

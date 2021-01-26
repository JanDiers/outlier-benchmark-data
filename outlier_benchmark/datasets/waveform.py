from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Waveform(BaseDataset):
    """
    The Waveform dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |  3443  |
    +-----------------------+--------+
    |number of features:    |   21   |
    +-----------------------+--------+
    |number of outliers:    |   100  |
    +-----------------------+--------+
    |percentage outliers:   |   2.9 %|
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named literature/Waveform/Waveform_withoutdupl_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import waveform
    >>> X, y = waveform.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (3443, 21)
    >>> y.sum()  # 100, the number of outliers in the dataset
    >>> X.max()  # 9.06
    >>> X.min()  # -4.2

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
    datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016). https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='Waveform', init=False)
    num_samples: int = field(default=3443, init=False)
    num_features: int = field(default=21, init=False)
    num_outlier: int = field(default=100, init=False)
    num_duplicates: int = field(default=0, init=False)


waveform = Waveform()

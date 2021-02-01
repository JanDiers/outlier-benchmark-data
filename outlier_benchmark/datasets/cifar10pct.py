from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar10pct(BaseDataset):
    """
    The Cifar10pct dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 3302   |
    +-----------------------+--------+
    |number of features:    |  200   |
    +-----------------------+--------+
    |number of outliers:    |  302   |
    +-----------------------+--------+
    |percentage outliers:   | 9.15 % |
    +-----------------------+--------+
    |number of duplicates:  |    21  |
    +-----------------------+--------+

    This dataset is based on the CIFAR-10 dataset, known from computer vision. On the test set, an [EfficientNet]_ was
    used to extract embeddings for the images. The EfficientNet was pretrained only on ImageNet data, no further
    training was conducted. See [MISSING_REF]_ for details. The inlier-classes consists of the following images:

    +-----------------------+------------+
    | class name            | n_images   |
    +-----------------------+------------+
    | automobile            |  1000      |
    +-----------------------+------------+
    | truck                 |  1000      |
    +-----------------------+------------+
    | ship                  |  1000      |
    +-----------------------+------------+
    | TOTAL INLIER          |  3000      |
    +-----------------------+------------+

    The outlier class consists of the following images:

    +-----------------------+------------+
    | class name            | n_images   |
    +-----------------------+------------+
    | horse                 |  151       |
    +-----------------------+------------+
    | airplane              |  151       |
    +-----------------------+------------+

    Usage:

    >>> from outlier_benchmark.datasets import cifar10pct
    >>> X, y = cifar10pct.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (50000, 27)
    >>> y.sum()  # 1508, the number of outliers in the dataset
    >>> X.max()  # 1.0
    >>> X.min()  # 0.0

    ..  [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
        International Conference on Machine Learning. PMLR, 2019.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar10pct', init=False)
    num_samples: int = field(default=3302, init=False)
    num_features: int = field(default=200, init=False)
    num_outlier: int = field(default=302, init=False)
    num_duplicates: int = field(default=21, init=False)


cifar10pct = Cifar10pct()

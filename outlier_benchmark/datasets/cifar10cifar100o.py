from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar10Cifar100O(BaseDataset):
    """
    The Cifar10Cifar100O dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 10000  |
    +-----------------------+--------+
    |number of features:    |  10    |
    +-----------------------+--------+
    |number of outliers:    |  1034  |
    +-----------------------+--------+
    |percentage outliers:   |100.0 % |
    +-----------------------+--------+
    |number of duplicates:  |   0    |
    +-----------------------+--------+

    This dataset is used for Out of Distribution Detection. Out of Distribution Detection aims to detect images
    that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on Cifar10 data. Afterwards, the model has been asked to predict
    on [Beans]_ data. The samples in this dataset contain predicitions of the trained EfficientNet on the Beans data.

    Note: All instances here are out-of-distribution data! Therefore, this dataset only contains outliers,
    and no inliers. The corresponding in-distribution-data is Cifar10O.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar10cifar100o
    >>> X, y = cifar10cifar100o.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (19968, 100)
    >>> y.sum()  #  the number of outliers in the dataset
    9984
    >>> X.max().round(2)
    0.99
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [Beans]  Makerere AI Lab, "Bean disease dataset.", online resource: https://github.com/AI-Lab-Makerere/ibean/.
       January 2020.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar10Cifar100O', init=False)
    num_samples: int = field(default=10000, init=False)
    num_features: int = field(default=10, init=False)
    num_outlier: int = field(default=0, init=False)
    num_duplicates: int = field(default=0, init=False)


cifar10cifar100o = Cifar10Cifar100O()

from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar10F(BaseDataset):
    """
    The Cifar10F dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 10000  |
    +-----------------------+--------+
    |number of features:    |  320   |
    +-----------------------+--------+
    |number of outliers:    |  0     |
    +-----------------------+--------+
    |percentage outliers:   |  0.0 % |
    +-----------------------+--------+
    |number of duplicates:  |   0    |
    +-----------------------+--------+

    This dataset is used for Out of Distribution Detection. Out of Distribution Detection aims to detect images
    that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on Cifar10 data. Afterwards, the model has been evaluated on the test
    data of Cifar10. The samples in this dataset contain feature-embeddings after the last convolutional layer of
    the trained EfficientNet.

    Note: All instances here are in-distribution data! Therefore, this dataset only contains inliers,
    and no outliers. There are many choices for out-of-distribution data. They all start with cifar10 and end on 'f',
    which stands for 'features'.

    * cifar10beansf
    * cifar10cifar100f
    * etc.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar10f
    >>> X, y = cifar10f.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (10000, 10)
    >>> y.sum()  #  the number of outliers in the dataset
    0
    >>> X.max().round(2)
    0.99
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar10F', init=False)
    num_samples: int = field(default=10000, init=False)
    num_features: int = field(default=10, init=False)
    num_outlier: int = field(default=0, init=False)
    num_duplicates: int = field(default=0, init=False)


cifar10f = Cifar10F()

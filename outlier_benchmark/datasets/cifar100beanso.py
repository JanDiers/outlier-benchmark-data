from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar100BeansO(BaseDataset):
    """
    The Cifar100BeansO dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 128    |
    +-----------------------+--------+
    |number of features:    |  100   |
    +-----------------------+--------+
    |number of outliers:    |  128   |
    +-----------------------+--------+
    |percentage outliers:   |100.0 % |
    +-----------------------+--------+
    |number of duplicates:  |   0    |
    +-----------------------+--------+

    This dataset is used for Out of Distribution Detection. Out of Distribution Detection aims to detect images
    that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on Cifar100 data. Afterwards, the model has been asked to predict
    on [Beans]_ data. The samples in this dataset contain predicitions of the trained EfficientNet on the Beans data.

    Note: All instances here are out-of-distribution data! Therefore, this dataset only contains outliers,
    and no inliers. The corresponding in-distribution-data is Cifar100O.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar100beanso
    >>> X, y = cifar100beanso.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (128, 100)
    >>> y.sum()  #  the number of outliers in the dataset
    128
    >>> X.max().round(2)
    0.86
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [Beans]  Makerere AI Lab, "Bean disease dataset.", online resource: https://github.com/AI-Lab-Makerere/ibean/.
       January 2020.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar100BeansO', init=False)
    num_samples: int = field(default=128, init=False)
    num_features: int = field(default=100, init=False)
    num_outlier: int = field(default=128, init=False)
    num_duplicates: int = field(default=0, init=False)


cifar100beanso = Cifar100BeansO()

from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar10BeansF(BaseDataset):
    """
    The Cifar10BeansF dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 1034   |
    +-----------------------+--------+
    |number of features:    |  320   |
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
    on [Beans]_ data. The samples in this dataset contain feature-embeddings after the last convolutional layer of
    the trained EfficientNet.

    Note: All instances here are out-of-distribution data! Therefore, this dataset only contains outliers,
    and no inliers. The corresponding in-distribution-data is Cifar10F.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar10beansf
    >>> X, y = cifar10beansf.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (1034, 320)
    >>> y.sum()  #  the number of outliers in the dataset
    1034
    >>> X.max().round(2)
    17.05
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [Beans]  Makerere AI Lab, "Bean disease dataset.", online resource: https://github.com/AI-Lab-Makerere/ibean/.
       January 2020.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar10BeansF', init=False)
    num_samples: int = field(default=1034, init=False)
    num_features: int = field(default=320, init=False)
    num_outlier: int = field(default=1034, init=False)
    num_duplicates: int = field(default=0, init=False)


cifar10beansf = Cifar10BeansF()

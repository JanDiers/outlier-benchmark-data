from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar10DtdO(BaseDataset):
    """
    The Cifar10DtdO dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 1880   |
    +-----------------------+--------+
    |number of features:    |  10    |
    +-----------------------+--------+
    |number of outliers:    |  1880  |
    +-----------------------+--------+
    |percentage outliers:   |100.0 % |
    +-----------------------+--------+
    |number of duplicates:  |   3    |
    +-----------------------+--------+

    This dataset is used for Out of Distribution Detection. Out of Distribution Detection aims to detect images
    that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on Cifar10 data. Afterwards, the model has been asked to predict
    on [DTD]_ data. The samples in this dataset contain predicitions of the trained EfficientNet on the Beans data.

    Note: All instances here are out-of-distribution data! Therefore, this dataset only contains outliers,
    and no inliers. The corresponding in-distribution-data is Cifar10O.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar10dtdo
    >>> X, y = cifar10dtdo.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (1880, 10)
    >>> y.sum()  #  the number of outliers in the dataset
    1880
    >>> X.max().round(2)
    0.88
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [DTD]  M.Cimpoi, S. Maji, I. Kokkinos, S. Mohamed, A. Vedaldi, "Describing Textures in the Wild".

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar10DtdO', init=False)
    num_samples: int = field(default=1880, init=False)
    num_features: int = field(default=10, init=False)
    num_outlier: int = field(default=1880, init=False)
    num_duplicates: int = field(default=3, init=False)


cifar10dtdo = Cifar10DtdO()

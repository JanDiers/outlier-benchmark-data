from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar10CitrusLeavesO(BaseDataset):
    """
    The Cifar10CitrusLeavesO dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 594    |
    +-----------------------+--------+
    |number of features:    |  10    |
    +-----------------------+--------+
    |number of outliers:    |  594   |
    +-----------------------+--------+
    |percentage outliers:   |100.0 % |
    +-----------------------+--------+
    |number of duplicates:  |   0    |
    +-----------------------+--------+

    This dataset is used for Out of Distribution Detection. Out of Distribution Detection aims to detect images
    that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on Cifar10 data. Afterwards, the model has been asked to predict
    on [CitrusLeaves]_ data. The samples in this dataset contain predicitions of the trained EfficientNet on the Beans data.

    Note: All instances here are out-of-distribution data! Therefore, this dataset only contains outliers,
    and no inliers. The corresponding in-distribution-data is Cifar10O.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar10citrusleaveso
    >>> X, y = cifar10citrusleaveso.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (594, 10)
    >>> y.sum()  #  the number of outliers in the dataset
    594
    >>> X.max().round(2)
    0.87
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [CitrusLeaves]  Rauf, Hafiz Tayyab; Saleem, Basharat ALi ; Lali, M. Ikram Ullah ; khan, attique; Sharif, Muhammad; Bukhari, Syed Ahmad Chan (2019), 
        "A Citrus Fruits and Leaves Dataset for Detection and Classification of Citrus Diseases through Machine Learning", Mendeley Data, V2, 
        doi: 10.17632/3f83gxmv57.2.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar10CitrusLeavesO', init=False)
    num_samples: int = field(default=594, init=False)
    num_features: int = field(default=10, init=False)
    num_outlier: int = field(default=594, init=False)
    num_duplicates: int = field(default=0, init=False)


cifar10citrusleaveso = Cifar10CitrusLeavesO()

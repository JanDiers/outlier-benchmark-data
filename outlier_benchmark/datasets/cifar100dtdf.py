from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar100DtdF(BaseDataset):
    """
    The Cifar100DtdF dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 1880   |
    +-----------------------+--------+
    |number of features:    |  320   |
    +-----------------------+--------+
    |number of outliers:    |  1880  |
    +-----------------------+--------+
    |percentage outliers:   |100.0 % |
    +-----------------------+--------+
    |number of duplicates:  |   3    |
    +-----------------------+--------+

    This dataset is used for Out of Distribution Detection. Out of Distribution Detection aims to detect images
    that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on Cifar100 data. Afterwards, the model has been asked to predict
    on [DTD]_ data. The samples in this dataset contain feature-embeddings after the last convolutional layer of
    the trained EfficientNet.

    Note: All instances here are out-of-distribution data! Therefore, this dataset only contains outliers,
    and no inliers. The corresponding in-distribution-data is Cifar100F.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar100dtdf
    >>> X, y = cifar100dtdf.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (1880, 320)
    >>> y.sum()  #  the number of outliers in the dataset
    1880
    >>> X.max().round(2)
    18.36
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [DTD]  M.Cimpoi, S. Maji, I. Kokkinos, S. Mohamed, A. Vedaldi, "Describing Textures in the Wild".

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar100DtdF', init=False)
    num_samples: int = field(default=1880, init=False)
    num_features: int = field(default=320, init=False)
    num_outlier: int = field(default=1880, init=False)
    num_duplicates: int = field(default=3, init=False)


cifar100dtdf = Cifar100DtdF()

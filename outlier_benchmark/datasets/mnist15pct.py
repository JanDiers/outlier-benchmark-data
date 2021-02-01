from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class MNIST15pct(BaseDataset):
    """
    The MNIST15pct.csv dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 3562   |
    +-----------------------+--------+
    |number of features:    |  50    |
    +-----------------------+--------+
    |number of outliers:    |  465   |
    +-----------------------+--------+
    |percentage outliers:   |13.05 % |
    +-----------------------+--------+
    |number of duplicates:  |   26   |
    +-----------------------+--------+

    This dataset is based on the MNIST dataset. On the test set, an [EfficientNet]_ was used to extract embeddings
    for the images. The EfficientNet was pretrained only on ImageNet data, no further
    training was conducted. See [MISSING_REF] for details. The inlier-classes consists of the following images:

    +-----------------------+------------+
    | class name            | n_images   |
    +-----------------------+------------+
    | 1                     |  1135      |
    +-----------------------+------------+
    | 0                     |  980       |
    +-----------------------+------------+
    | 4                     |  982       |
    +-----------------------+------------+
    | TOTAL INLIER          |  3097      |
    +-----------------------+------------+

    The outlier class consists of the following images:

    +-----------------------+------------+
    | class name            | n_images   |
    +-----------------------+------------+
    | 8                     |  155       |
    +-----------------------+------------+
    | 9                     |  155       |
    +-----------------------+------------+
    | 6                     |  155       |
    +-----------------------+------------+

    Usage:

    >>> from outlier_benchmark.datasets import mnist15pct
    >>> X, y = mnist15pct.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (50000, 27)
    >>> y.sum()  # 1508, the number of outliers in the dataset
    >>> X.max()  # 1.0
    >>> X.min()  # 0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='MNIST15pct', init=False)
    num_samples: int = field(default=3562, init=False)
    num_features: int = field(default=50, init=False)
    num_outlier: int = field(default=465, init=False)
    num_duplicates: int = field(default=26, init=False)


mnist15pct = MNIST15pct()

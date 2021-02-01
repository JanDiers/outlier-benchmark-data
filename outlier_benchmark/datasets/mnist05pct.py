from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class MNIST05pct(BaseDataset):
    """
    The MNIST05pct dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 3252   |
    +-----------------------+--------+
    |number of features:    |  50    |
    +-----------------------+--------+
    |number of outliers:    |  155   |
    +-----------------------+--------+
    |percentage outliers:   | 4.77 % |
    +-----------------------+--------+
    |number of duplicates:  |    7   |
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

    Usage:

    >>> from outlier_benchmark.datasets import mnist05pct
    >>> X, y = mnist05pct.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (3252, 50)
    >>> y.sum()  # the number of outliers in the dataset
    155
    >>> X.max().round(2)
    6.9
    >>> X.min().round(2)
    -6.43

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='MNIST05pct', init=False)
    num_samples: int = field(default=3252, init=False)
    num_features: int = field(default=50, init=False)
    num_outlier: int = field(default=155, init=False)
    num_duplicates: int = field(default=7, init=False)


mnist05pct = MNIST05pct()

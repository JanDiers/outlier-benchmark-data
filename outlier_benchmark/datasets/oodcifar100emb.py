from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class OODCifar100Emb(BaseDataset):
    """
    The OODCifar100Emb dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 19968  |
    +-----------------------+--------+
    |number of features:    |  308   |
    +-----------------------+--------+
    |number of outliers:    |  9984  |
    +-----------------------+--------+
    |percentage outliers:   |50.0 %  |
    +-----------------------+--------+
    |number of duplicates:  |   0    |
    +-----------------------+--------+

    Out of Distribution Detection aims to detect images that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on the Cifar100 data. The first part of the data contains predictions
    of the model on the test set of Cifar100. The second part of the data is predictions run on
    Street View house numbers. The neural network was not trained to recognize house numbers, so this is
    an example for out-of-distribution detection.

    The features in this dataset are intermediate features after all convolutional operations have been performed. It is
    taken before the dense layer at the end of the network.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import oodcifar100
    >>> X, y = oodcifar100.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (3562, 50)
    >>> y.sum()  #  the number of outliers in the dataset
    465
    >>> X.max().round(2)
    6.9
    >>> X.min().round(2)
    -6.43

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='OODCifar100Emb', init=False)
    num_samples: int = field(default=19968, init=False)
    num_features: int = field(default=308, init=False)
    num_outlier: int = field(default=9984, init=False)
    num_duplicates: int = field(default=0, init=False)


oodcifar100emb = OODCifar100Emb()

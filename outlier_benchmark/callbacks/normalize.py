import numpy as np

from outlier_benchmark.callbacks.base.callback import BaseCallback


class NormalizeCallback(BaseCallback):

    def __init__(self, minimum: float = 0., maximum: float = 1.):
        """
        The NormalizeCallback normalizes every feature to have a minimum value of 0 and a maximum value of 1.

        The minimum and maximum value may be chosen according the parameters.

        Example:

        >>> from outlier_benchmark.datasets import aloi
        >>> from outlier_benchmark.callbacks import NormalizeCallback
        >>> X, y = aloi.add_callback(NormalizeCallback(minimum=0, maximum=5)).load()
        >>> X.min(), X.max()
        >>> # (0.0, 5.0)

        :param minimum: float, minimum value for features
        :param maximum: float, maximum value for features
        """
        self.minimum = minimum
        self.maximum = maximum

    def after_load(self, dataset, X, y):

        # take care of zero divisions
        scale = X.max(axis=0) - X.min(axis=0)

        # calculuate nominator
        X = ((X - X.min(axis=0)) * (self.maximum - self.minimum))

        # divide if not zero. if zero: output 0. transform to the desired minimum value.
        X = self.minimum + np.divide(X, scale, out=np.zeros_like(X), where=scale != 0)

        return dataset, X, y

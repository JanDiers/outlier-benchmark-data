class BaseCallback:
    """

    The BaseCallback serves as abstract class to implement callbacks. You can also create your own callbacks
    by inheriting from this callback.

    Example:

    >>> from outlier_benchmark.callbacks.base import BaseCallback
    >>> from outlier_benchmark.datasets import cardiotocography
    >>> # data without your callback
    >>> X, y = cardiotocography.load()
    >>> X.min(), X.max()  # (-1.0, 564.0)
    >>> # write your callback which shifts every feature
    >>> class MyShiftFeaturesCallback(BaseCallback):
    >>>    def __init__(self, shift_by: int = -50):
    >>>        self.shift_by = shift_by
    >>>
    >>>    def after_load(self, dataset, X, y):
    >>>        X = X + self.shift_by
    >>>        return dataset, X, y
    >>> # add your callback to the dataset
    >>> cardiotocography.add_callback(MyShiftFeaturesCallback())
    >>> # load the data
    >>> X, y = cardiotocography.load()
    >>> X.min(), X.max()  # (-51.0, 514.0)

    """

    def before_load(self, dataset):
        """
        This method is called before dataset.load() is called.

        :param dataset: the dataset
        :return: dataset
        """
        return dataset

    def after_load(self, dataset, X, y):
        """
        This method is called after dataset.load() has been called.

        :param dataset: the dataset
        :param X: the X data of the dataset
        :param y: the y data of the dataset
        :return: dataset, X and y
        """
        return dataset, X, y

    def __str__(self):
        attributes = vars(self)
        attributes = ', '.join([f'{attr}={val}' for attr, val in attributes.items()])
        return f'{self.__class__.__name__}({attributes})'

from dataclasses import dataclass, field, replace

from outlier_benchmark.datasets.base import BaseDataset


@dataclass
class DatasetCollection:
    """

    The DatasetCollection is useful if you want to test your algorithms on different datasets. We have provided some
    default filters so you can only include those datasets you are interested in. You can also apply your own filter
    logic by using the LambdaFilter method of this collection.

    Example usage:

    >>> from outlier_benchmark.data_collection import DatasetCollection
    >>> collection = DatasetCollection()

    By default, the DatasetCollection is initialized with all datasets. If you want to filter the collection so it fits
    your needs, you may use predefined methods or LambdaFilter method:

    >>> collection = collection.num_features(maximum=15).num_samples(minimum=50)
    >>> collection  # doctest: +SKIP
    DatasetCollection(n_datasets=15, filters_applied=['num_features', 'num_samples'])

    At this point you can load the remaining datasets in a for loop and test it against your algorithms:

    >>> for dataset in collection:  # doctest: +SKIP
    ...        X, y = dataset.load()
    ...        # do anything here for every dataset

    If you make use of custom Datasets, they will be recognized automatically and included in this Collection. Example:

    >>> from dataclasses import dataclass
    >>> from outlier_benchmark.datasets.base import BaseDataset

    Implement any dataset you need, see the :doc:`guide <custom_datasets>` for further instructions

    >>> @dataclass
    ... class MyNewDataset(BaseDataset):
    ...     name: str = 'Any Name'
    ...     num_samples: int = 444
    ...     num_features: int = 333
    ...     num_outlier: int = 222
    ...     num_duplicates: int = 111

    When you load the collection, your newly created dataset will be there:

    >>> collection = DatasetCollection()
    >>> MyNewDataset() in collection
    True
    >>> collection[-1]  # doctest: +ELLIPSIS
    MyNewDataset(name='Any Name', num_samples=444, ...)

    """

    datasets: list = field(default_factory=lambda: [dataset() for dataset in BaseDataset._derived_datasets], repr=False)
    n_datasets: int = field(init=False)
    filters_applied: list = field(default_factory=lambda: [])

    def __post_init__(self):
        self.n_datasets = len(self)

    def __iter__(self) -> BaseDataset:
        yield from self.datasets

    def __len__(self):
        return len(self.datasets)

    def __contains__(self, item):
        return item in self.datasets

    def __getitem__(self, item) -> BaseDataset:
        return self.datasets[item]

    def LambdaFilter(self, filter_function: callable):
        """
        Applies arbitrary filter logic to the DatasetCollection. The function passed to this method determines if the
        dataset remains in the dataset. If fun(dataset) evaluates to True, the dataset remains in the collection,
        otherwise it will be removed.

        Example:

        >>> from outlier_benchmark.data_collection import DatasetCollection
        >>> ds = DatasetCollection()
        >>> ds = ds.LambdaFilter(lambda dataset: 'MNIST' in dataset.name)  # only MNIST datasets
        >>> ds
        DatasetCollection(n_datasets=3, filters_applied=['<lambda>'])
        >>> ds = ds.pct_outlier(maximum=5.0)  # only MNIST datasets with maximum of 5 percentage outlier
        >>> ds
        DatasetCollection(n_datasets=1, filters_applied=['<lambda>', 'pct_outlier'])


        :param filter_function: function to evaluate on each dataset in the collection
        :return: DatasetCollection
        """

        new_set = list(filter(filter_function, self.datasets))
        filters_applied = self.filters_applied + [filter_function.__name__]
        if len(new_set) == 0:
            raise ValueError('No datasets remained after applying filters:', filters_applied)
        ds = replace(self, datasets=new_set, filters_applied=filters_applied)
        return ds

    def num_samples(self, minimum: int = 0, maximum: int = float('inf')) -> 'DatasetCollection':
        """
        Removes all datasets from the collection if they do not have at least min|max samples

        :param minimum: minimum number of samples. defaults to 0.
        :param maximum: maximum number of samples. defaults to infinity.

        :return: DatasetCollection
        """

        def num_samples(d):
            return minimum <= d.num_samples <= maximum

        return self.LambdaFilter(num_samples)

    def num_features(self, minimum: int = 0, maximum: int = float('inf')) -> 'DatasetCollection':
        """
        Removes all datasets from the collection if they do not have at least min|max features

        :param minimum: minimum number of features. defaults to 0.
        :param maximum: maximum number of features. defaults to infinity.

        :return: DatasetCollection
        """

        def num_features(d):
            return minimum <= d.num_features <= maximum

        return self.LambdaFilter(num_features)

    def num_outlier(self, minimum: int = 0, maximum: int = float('inf')) -> 'DatasetCollection':
        """
        Removes all datasets from the collection if they do not have at least min|max outliers

        :param minimum: minimum number of outliers. defaults to 0.
        :param maximum: maximum number of outliers. defaults to infinity.

        :return: DatasetCollection
        """

        def num_outlier(d):
            return minimum <= d.num_outlier <= maximum

        return self.LambdaFilter(num_outlier)

    def num_duplicates(self, minimum: int = 0, maximum: int = float('inf')) -> 'DatasetCollection':
        """
        Removes all datasets from the collection if they do not have at least min|max duplicates

        :param minimum: minimum number of duplicates. defaults to 0.
        :param maximum: maximum number of duplicates. defaults to infinity.

        :return: DatasetCollection
        """

        def num_duplicates(d):
            return minimum <= d.num_duplicates <= maximum

        return self.LambdaFilter(num_duplicates)

    def pct_outlier(self, minimum: float = 0.0, maximum: float = 100.0) -> 'DatasetCollection':
        """
        Removes all datasets from the collection if they do not have at least min|max percentage of outliers

        :param minimum: minimum percentage of outliers. defaults to 0.
        :param maximum: maximum percentage of outliers. defaults to 100.

        :return: DatasetCollection
        """

        def pct_outlier(d):
            return minimum <= d.pct_outlier <= maximum

        return self.LambdaFilter(pct_outlier)

"""

If you want to create and load datasets on your own, it is easy. You have to inherit from :py:class:`BaseDataset`
and overwrite the :py:meth:`load()` method.

Example:

>>> from dataclasses import dataclass
>>> import numpy as np
>>> from outlier_benchmark.datasets.base import BaseDataset
>>> from outlier_benchmark.data_collection import DatasetCollection

Do not forget to set the `@dataclass <https://docs.python.org/3/library/dataclasses.html>`_ decorator:

>>> @dataclass  # doctest: +SKIP
... class MyNewDataset(BaseDataset):
...     name = 'Any Name you like'
...     num_samples = 50
...     num_features = 5
...     num_outlier = 7
...     num_duplicates = 15
...     other_things = 'anything'
...     or_even_more = False


The attributes you set here are used for displaying the properties of your dataset as well as filtering in
:doc:`dataset_collection`.

However, you just defined the properties of the dataset. How do you load the data? For this, you only have to overwrite
the load() method of your MyNewDataset class. Update the class as follows:

>>> @dataclass
... class MyNewDataset(BaseDataset):
...     name = 'Any Name you like'
...     num_samples = 50
...     num_features = 5
...     num_outlier = 7
...     num_duplicates = 0
...     other_things = 'anything'
...     or_even_more = False
...
...     def load(self, *args):
...         # place any loading procedure here, e.g. loading csv files or download from remote
...         # we use some dummy data
...         X = np.random.randn(50, 5)
...         y = np.array([0] * 43 + [1] * 7)
...         return X, y

At this point, the DatasetCollection is already aware you created this dataset:

>>> collection = DatasetCollection()
>>> MyNewDataset() in collection
True

You can now load the data:

>>> mydata = MyNewDataset()
>>> X, y = mydata.load()

"""

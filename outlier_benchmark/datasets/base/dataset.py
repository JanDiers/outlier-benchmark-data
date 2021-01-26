import functools
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd

from outlier_benchmark.callbacks.base.callback import BaseCallback
from outlier_benchmark.callbacks.normalize import NormalizeCallback


def load_callbacks(load):
    @functools.wraps(load)
    def call_load(*args, **kwargs):
        dataset: BaseDataset = args[0]

        # execute callbacks before load
        for callback in dataset.callbacks:
            if hasattr(callback, 'before_load'):
                dataset = callback.before_load(dataset)

        X, y = load(*args, **kwargs)

        # execute callbacks before load
        for callback in dataset.callbacks:
            if hasattr(callback, 'after_load'):
                dataset, X, y = callback.after_load(dataset, X, y)

        return X, y

    return call_load


@dataclass
class BaseDataset:
    name: str = field(init=False)
    num_samples: int
    num_features: int
    num_outlier: int
    num_duplicates: int
    pct_outlier: float = field(init=False)
    callbacks: list = field(default_factory=lambda: [], repr=False)

    @property
    def path(self) -> Path:
        from outlier_benchmark.config import DATA_HOME
        cls_name = self.__class__.__name__
        return DATA_HOME / cls_name / (cls_name + '.csv')

    def __post_init__(self):
        self.pct_outlier = round((self.num_outlier / self.num_samples) * 100, 2)

    @load_callbacks
    def load(self, download: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        """
        loads the data X and y, both numpy arrays. If not previously downloaded and ``download=True``, before loading
        the dataset will be downloaded to your local machine.

        :param download: bool, if download is allowed
        :return: X and y, both numpy arrays.
        """
        if not self.path.exists():
            if download:
                self._download()
            else:
                raise ValueError(f'WBC data has not yet been downloaded to your machine and you passed download=False. '
                                 f'Pass download=True to download and load data.')

        df = pd.read_csv(self.path)
        X = df.drop('outlier', axis=1).values
        y = df['outlier'].values
        return X, y

    def remove_callbacks(self):
        self.callbacks = []

    def add_callback(self, callback: BaseCallback) -> 'BaseDataset':
        """
        Adds the callback to the dataset. Callbacks are executed in the order they are added.

        :param callback: callback,
        :return: None
        """

        if not isinstance(callback, BaseCallback):
            raise ValueError(f'Can only add instances of Callbacks as callback. You passed: {type(callback)}')

        self.callbacks.append(callback)

        return self

    def normalize(self, min: float = 0, max: float = 1) -> 'BaseDataset':
        """
        Normalizes the data after loading to the range (min, max).

        Note: This is a shortcut to add a call. It is equvivalent to call
        ``add_callback(NormalizeCallback(minimum=min, maximum=max))``.

        Example (using the waveform dataset):

        >>> from outlier_benchmark.datasets import waveform
        >>> X, y = waveform.normalize(min=0, max=1).load()
        >>> X.min, X.max()  # (0, 1)
        >>> # you can also scale to arbitrary ranges:
        >>> X, y = waveform.normalize(-0.55, 10.7).load()
        >>> X.min, X.max()  # (-0.55, 10.7)

        :param min: minmum value for every feature
        :param max: maximum value for every feature
        :return: self
        """
        self.add_callback(NormalizeCallback(minimum=min, maximum=max))
        return self

    def _download(self):
        from outlier_benchmark.config import DOWNLOAD_BASE_URL, DATA_HOME
        download_from = self.path.relative_to(DATA_HOME)

        url = DOWNLOAD_BASE_URL + '/' + download_from.as_posix()

        print('download from', url, '...')

        response = urllib.request.urlopen(url)
        data = response.read()  # a `bytes` object
        text = data.decode('utf-8')

        # make path
        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.path.write_text(text, encoding='utf-8')

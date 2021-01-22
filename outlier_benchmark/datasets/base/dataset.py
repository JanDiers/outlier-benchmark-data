import functools
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd

from outlier_benchmark.callbacks.base.callback import BaseCallback


def _callbacks_on(dataset_method: str):
    """
    This function serves as decorator for dataset methods. It ensures:
    - callback.before_{dataset_method} is called
    - dataset.{method} is called
    - callback.after_{dataset_method} is called.

    The results are returned.

    :param dataset_method: name of the dataset method, e.g. 'load'
    :return: decorated method
    """
    def decorated_method(func):
        @functools.wraps(func)
        def wrap_decorated(*args, **kwargs):
            dataset: BaseDataset = args[0]

            # execute callbacks before method
            for callback in dataset.callbacks:
                if hasattr(callback, f'before_{dataset_method}'):
                    method = getattr(callback, f'before_{dataset_method}')
                    method(dataset)

            # execute method
            value = func(*args, **kwargs)

            # execute callbacks after method
            for callback in dataset.callbacks:
                if hasattr(callback, f'after_{dataset_method}'):
                    method = getattr(callback, f'after_{dataset_method}')
                    method(dataset, *value)

            return value
        return wrap_decorated
    return decorated_method


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

    @_callbacks_on('load')
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

    def add_callback(self, callback: BaseCallback) -> None:
        """
        Adds the callback to the dataset. Callbacks are executed in the order they are added.

        :param callback: callback,
        :return: None
        """
        self.callbacks.append(callback)

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

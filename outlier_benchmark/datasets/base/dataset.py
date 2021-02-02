import functools
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd


@dataclass
class BaseDataset:
    name: str = field(init=False)
    num_samples: int = field(init=False)
    num_features: int = field(init=False)
    num_outlier: int = field(init=False)
    num_duplicates: int = field(init=False)
    pct_outlier: float = field(init=False)

    _derived_datasets = []

    def __init_subclass__(cls, **kwargs):
        """
        class method that registers every derived subclass. This method is needed to load all datasets in a
        DatasetColelction.

        :param kwargs: passed
        :return: None

        """
        super().__init_subclass__(**kwargs)
        cls._derived_datasets.append(cls)

    @property
    def path(self) -> Path:
        from outlier_benchmark.config import DATA_HOME
        cls_name = self.__class__.__name__
        return DATA_HOME / cls_name / (cls_name + '.csv')

    def __post_init__(self):
        self.pct_outlier = round((self.num_outlier / self.num_samples) * 100, 2)

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
        y = df['outlier'].values.astype(int)
        return X, y

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

import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd


@dataclass
class BaseDataset:
    name: str
    num_samples: int
    num_features: int
    num_outlier: int
    number_duplicates: int
    pct_outlier: float = field(init=False)

    @property
    def path(self) -> Path:
        from outlier_benchmark.config import DATA_HOME
        cls_name = self.__class__.__name__
        return DATA_HOME / cls_name / (cls_name + '.csv')

    def __post_init__(self):
        self.pct_outlier = round((self.num_outlier / self.num_samples) * 100, 2)

    def load(self, download: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        """
        loads the data X and y, both numpy arrays. If not previously downloaded and download = True, before loading
        the dataset will be downloaded to your local machine.

        Example:
        >>> from outlier_benchmark.datasets import wbc
        >>> X, y = wbc.load(download=True)  # download will only take place if not previously downloaded
        >>> X.shape  # (454, 9)

        :param download: bool, if download is allowed
        :return: X and y, both numpy arrays.
        """
        if not self.path.exists():
            if download:
                self.download()
            else:
                raise ValueError(f'WBC data has not yet been downloaded to your machine and you passed download=False. '
                                 f'Pass download=True to download and load data.')

        df = pd.read_csv(self.path)
        X = df.drop('outlier', axis=1).values
        y = df['outlier'].values
        return X, y

    def download(self):
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

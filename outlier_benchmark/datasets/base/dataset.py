import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

import numpy as np

from outlier_benchmark.datasets.base.load import get_data_home


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
        return DATA_HOME /cls_name / (cls_name + '.csv')

    def __post_init__(self):
        self.pct_outlier = round(self.num_outlier / self.num_samples, 4)

    def load(self, download: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        raise NotImplementedError('You are trying to load an abstract class. '
                                  'You must load one of the subclasses of BaseDataset.')

    def download(self):
        from outlier_benchmark.config import DOWNLOAD_BASE_URL, DATA_HOME
        download_from = self.path.relative_to(DATA_HOME)

        url = DOWNLOAD_BASE_URL + '/' + download_from.as_posix()
        response = urllib.request.urlopen(url)
        data = response.read()      # a `bytes` object
        text = data.decode('utf-8')

        self.path.write_text(text, encoding='utf-8')

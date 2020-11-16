import re
from collections import namedtuple
from typing import Union, Tuple

import numpy as np

from outlier_benchmark.data.list_of_files import all_files
from outlier_benchmark.data.load_data import load


def get_percent(filename: str) -> Union[None, float]:
    percent = re.findall(r'_\d\d', filename)
    if percent:
        percent = percent[0]
        percent = re.sub(r'_', '', percent)
        percent = float(percent)
    return percent or None


def get_vnum(filename: str) -> float:
    vnum = re.findall(r'_v\d+', filename)
    if vnum:
        vnum = vnum[0]
        vnum = re.sub(r'_v', '', vnum)
        vnum = float(vnum)
    else:
        vnum = 0.
    return vnum


def get_norm(filename: str) -> bool:
    return '_norm' in filename


def get_name(filename: str) -> str:
    return filename.split('_')[0]


BaseDataset = namedtuple('BaseDataset', ['filename', 'name', 'norm', 'percent', 'vnum'])


class Dataset(BaseDataset):
    def load(self) -> Tuple[np.ndarray, np.ndarray]:
        return load(self.filename)


class DatasetCollection(list):
    def __init__(self, datasets: filter = None):
        if datasets is None:  # build all datasets
            datasets = [Dataset(
                filename=filename, name=get_name(filename),
                norm=get_norm(filename), percent=get_percent(filename), vnum=get_vnum(filename)
            ) for filename in all_files]

        super().__init__(datasets)

    def _highest_vnum(self):
        remove_vnum = lambda f: re.sub(r'_v\d+', '', f)
        all_without_versions = set([remove_vnum(d.filename) for d in self])

        for variant in all_without_versions:
            highest_vnum = max([d.vnum for d in self if remove_vnum(d.filename) == variant])
            for d in self:
                if remove_vnum(d.filename) == variant and d.vnum == highest_vnum:
                    yield d

    def vnum(self, num: float = -1):
        """
        Filter datasets for version number. num=-1 for highest version available per dataset name.

        :param num: version number, for highest version take -1
        :return: Datasets
        """
        if num > 0:
            accept = lambda d: d.vnum == num
            return DatasetCollection(filter(accept, self))

        else:
            return DatasetCollection(self._highest_vnum())

    def percent(self, min_pct: float = None, max_pct: float = None, include_unknown: bool = True):

        if max_pct is None:
            max_pct = 100.
        if min_pct is None:
            min_pct = 0.

        if min_pct > max_pct:
            raise ValueError(f'min_pct must be lower than max_pct. Found: min_pct={min_pct} > {max_pct}=max_pct')

        if max([min_pct, max_pct]) < 1:
            raise UserWarning(f'Percentage expected to be in range 0...100. You passed at max {max_pct}')

        r = self

        if min_pct:
            accept = lambda d: ((d.percent is None) and include_unknown) or (d.percent >= min_pct)
            r = filter(accept, r)

        if max_pct:
            accept = lambda d: ((d.percent is None) and include_unknown) or (d.percent <= max_pct)
            r = filter(accept, r)

        return DatasetCollection(r)

    def norm(self, norm: bool):
        accept = lambda d: d.norm == norm
        r = filter(accept, self)
        return DatasetCollection(r)

    def name(self, name: str):
        all_names = [d.name for d in self]

        if name not in all_names:
            raise ValueError(f'No dataset with name {name} left. Total number of datasets available: {len(all_names)}')

        accept = lambda d: d.name == name
        r = filter(accept, self)
        return DatasetCollection(r)

    def withoutdupl(self, withoutdupl: bool):
        if withoutdupl:
            accept = lambda d: '_withoutdupl' in d.filename
        else:
            accept = lambda d: '_withoutdupl' not in d.filename

        return DatasetCollection(filter(accept, self))

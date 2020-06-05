from outlier_benchmark.data.download_from_remote import get_data_home
from outlier_benchmark.data.file_loader import CsvFileLoader, ArffFileLoader, MatFileLoader
from pathlib import Path
import numpy as np


def folder(name: str) -> Path:
    folder = name.split('_')[0]
    return Path(folder)


def file_type(name: str) -> str:
    return name.split('.')[-1]


_file_loader = dict(
    arff=ArffFileLoader,
    csv=CsvFileLoader,
    mat=MatFileLoader,
)


def load(name: str, data_home=None) -> np.Array:
    home = get_data_home(data_home=data_home)
    file_path = home.joinpath(folder(name)).joinpath(name)

    file_loader = _file_loader.get(file_type(name), None)
    if not file_loader:
        raise ValueError(f'No file loader found for file type {file_type(name)}')

    file_loader = file_loader(name, file_path)
    X, y = file_loader.load()

    return X, y






data_home = None
name = 'Shuttle_withoutdupl_norm_v10.arff'












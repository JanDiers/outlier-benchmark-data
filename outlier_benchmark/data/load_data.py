from typing import Tuple, List
from outlier_benchmark.data.download_from_remote import get_data_home, download
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


def list_available_files() -> List[str]:
    """
    lists all files that are available, either already offline on your system or online to download
    :return: list of all files: List[str]
    """
    from outlier_benchmark.files.list_of_files import all_files
    return all_files


def load(name: str, data_home=None) -> Tuple[np.ndarray, np.ndarray]:
    """
    loads the data with the given name. Get a list of available data sets by using list_available_files().

    :param name: name of the dataset. include the file ending.
    :param data_home: if not specified, defaults to the home directory of the user.
    :return: (X, y), both are numpy arrays
    """

    if name not in list_available_files():
        raise ValueError(f'{name} is not a supported data set. Check for typos.')

    home = get_data_home(data_home=data_home)
    file_path = home.joinpath(folder(name)).joinpath(name)

    if not file_path.exists():
        download(filename=name, data_home=data_home)

    file_loader = _file_loader.get(file_type(name), None)
    if not file_loader:
        raise ValueError(f'No file loader found for file type {file_type(name)}')

    file_loader = file_loader(name, file_path)
    X, y = file_loader.load()

    return X, y

from os import environ, makedirs, sep
from os.path import exists, expanduser, join
from pathlib import Path


def get_data_home(data_home=None) -> Path:
    """Return the path where the outlier data sets are downloaded to. Function adapted from scikit-learns data set API.

    Parameters
    ----------
    data_home : str | None
        The path to the data.
    """
    if data_home is None:
        data_home = environ.get('.OUTLIER_BENCHMARK_DATA' + sep + 'FILES',
                                join('~', '.outlier_benchmark_data' + sep + 'files'))
    data_home = expanduser(data_home)
    if not exists(data_home):
        makedirs(data_home)

    data_home = Path(data_home)

    return data_home

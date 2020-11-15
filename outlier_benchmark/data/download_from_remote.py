from os import environ, makedirs, sep
from os.path import exists, expanduser, join
from pathlib import Path
import urllib.request


DOWNLOAD_BASE_URL = 'https://raw.githubusercontent.com/JanDiers/outlier-benchmark-data/master/outlier_benchmark/files/'


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


def download(filename: str, data_home=None):
    data_home = get_data_home(data_home)

    folder = filename.split('_')[0]

    url = DOWNLOAD_BASE_URL + folder + '/' + filename
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8')

    path = data_home / folder / filename

    path.write_text(text, encoding='utf-8')

from typing import Tuple

import numpy as np
import pandas as pd
from scipy.io.arff import loadarff


class FileLoader:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path


class ArffFileLoader(FileLoader):
    """
    Class for loading arff-files
    :param name: name of data set. used for representation.
    :param path: file path for arff file
    """

    def load(self) -> Tuple[np.array, np.array]:
        # read arff
        data = loadarff(self.path)

        # cast to dataframe
        df = pd.DataFrame(data[0])

        # set index
        df = df.set_index('id')

        # encode string representation
        cols = df.select_dtypes(include=['object']).columns
        df[cols] = df[cols].applymap(lambda x: x.decode())

        target = 'outlier'
        try:
            df[target].replace({"yes": 1, "no": 0}, inplace=True)
        except KeyError:
            target = 'Outlier'
            df[target].replace({"yes": 1, "no": 0}, inplace=True)

        X = df.drop(target, 1).values
        y = df[target].values

        return X, y


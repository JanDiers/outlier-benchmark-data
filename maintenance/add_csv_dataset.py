import os
from pathlib import Path

import pandas as pd

from maintenance.add_to_libraray import add_to_init
from maintenance.template_description import get_template_description


OUTPUT_PATH = Path('./..') / 'outlier_benchmark/new_files/'
DOWNLOAD_BASE_URL = 'https://raw.githubusercontent.com/JanDiers/outlier-benchmark-data/master/outlier_benchmark/files/'


def write_dataset(X, y, name: str, specification: str = None, lmu_name: str = None):

    write_dir = OUTPUT_PATH / name

    if specification:
        write_dir = write_dir / specification

    # check no dataset is already registered under the name
    if write_dir.exists():
        raise ValueError(f'Dataset with name {name} '
                         + (f'and specification {specification} ' if specification else '')
                         + 'already exists. '
                         + ('You may choose a specification, if you like.' if not specification else
                            'Choose another specification.')
                         + os.linesep + os.linesep + 'No output has been written.' + os.linesep
                         )

    # make directories to store the data
    write_dir.mkdir(parents=True)

    # stack together X and y with feature names and target name
    feature_columns_names = [f'feature_{i}' for i in range(1, X.shape[1] + 1)]
    target_column_name = 'target'
    data = pd.DataFrame(X, columns=feature_columns_names)
    data[target_column_name] = y

    # store the data to folder
    data.to_csv(write_dir / 'data.csv', index=False)

    # make description file
    description_file = write_dir / 'template_description.rst'

    new_description = True
    if description_file.exists():
        keep = 'x'
        while keep not in ['y', 'n']:
            keep = input(
                f'Description file for {name} {"and specification" + specification if specification else ""} '
                f'already exists. Do you want to keep the current description? (y/n)')

            if keep not in ['y', 'n']:
                print('Please enter y or n. Try again.')

        new_description = True if keep == 'n' else False

    if new_description:
        print('Creating new description file at', description_file)
        download_link = DOWNLOAD_BASE_URL + name + '/data.csv'
        class_name = name
        if specification:
            class_name += f'{specification}pct'
        description = get_template_description(name, class_name=class_name, n_samples=data.shape[0], n_features=data.shape[1], n_outlier=y.sum(),
                                               download_link=download_link, lmu_name=lmu_name)
        description_file.write_text(description)
    else:
        print('I am not creating a new description file.')

    # add to dataset.__init__.py
    class_name = name
    if specification:
        class_name += f'{specification}pct'

    add_to_init(class_name, name, data.shape[0], data.shape[1], y.sum(), file_path=str(write_dir).replace('\\', '/'))


if __name__ == "__main__":
    from outlier_benchmark.data.datasets.dataset import DatasetCollection
    for dataset in DatasetCollection().vnum(-1):
        X, y = dataset.load()
        specification = None if dataset.percent is None else str(int(dataset.percent))
        lmu_name = dataset.filename.split('.')[0]
        try:
            write_dataset(X, y, name=dataset.name, lmu_name=lmu_name, specification=specification)
        except ValueError:
            continue


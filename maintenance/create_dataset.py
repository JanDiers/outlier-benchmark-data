import os
from pathlib import Path

import pandas as pd

from maintenance.loader import ArffFileLoader


def make_package_for_data(path):
    name = Path(path).stem

    if '_' in name:
        name = name.split('_')[0]

    loader = ArffFileLoader(name=name, path=path)

    X, y = loader.load()

    num_samples, num_features = X.shape
    num_outlier: int = y.sum()
    num_duplicates: int = pd.DataFrame(X).duplicated().sum()

    save_to = Path.cwd() / 'files' / name
    save_to.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(X, columns=[f'feature_{i + 1}' for i in range(num_features)])
    df['outlier'] = y
    df.to_csv(save_to / (name + '.csv'), index=False)

    template = f'''
    from dataclasses import dataclass
    
    from outlier_benchmark.datasets.base.dataset import BaseDataset
    
    
    @dataclass
    class {name}(BaseDataset):
        """
        The {name} dataset has the following properties:
    
        +-----------------------+--------+
        |number of samples:     |   {num_samples}  |
        +-----------------------+--------+
        |number of features:    |   {num_features}    |
        +-----------------------+--------+
        |number of outliers:    |   {num_outlier}   |
        +-----------------------+--------+
        |percentage outliers:   |   {round(num_outlier / num_samples, 4) * 100} %|
        +-----------------------+--------+
        |number of duplicates:  |   {num_duplicates}  |
        +-----------------------+--------+
    
    
        This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
        The dataset provided here is a copy of the dataset taken from the
        `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.
    
        No further preprocessing has been applied. The file is named {Path(path).relative_to('tempdata').as_posix()} in the
        collection of [1]_.
    
        Usage:
    
        >>> from outlier_benchmark.datasets import {name.lower()}
        >>> X, y = {name.lower()}.load(download=True)  # download will only take place if not previously downloaded
        >>> X.shape  # ({num_samples}, {num_features})
        >>> y.sum()  # {y.sum()}, the number of outliers in the dataset
        >>> X.max()  # {X.max()}
        >>> X.min()  # {X.min()}
    
        ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
            by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenková, E. Schubert, I. Assent and M. E. Houle
            Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8
    
        """
    
        name: str = '{name}'
        num_samples: int = {num_samples}
        num_features: int = {num_features}
        num_outlier: int = {num_outlier}
        number_duplicates: int = {num_duplicates}
    
    '''

    folder = Path('outlier_benchmark/datasets') / ('_' + name)
    folder.mkdir(parents=True, exist_ok=True)

    (folder / (name.lower() + '.py')).write_text(template, encoding='windows-1252')

    init = f'from .{name.lower()} import {name}{os.linesep + os.linesep}{name.lower()} = {name}(){os.linesep + os.linesep}__all__ = [{name.lower()}]'

    (folder / '__init__.py').write_text(init)


all_paths = [
    'tempdata/literature/ALOI/ALOI.arff',
    'tempdata/literature/Glass/Glass_withoutdupl_norm.arff',
    'tempdata/literature/Ionosphere/Ionosphere_withoutdupl_norm.arff',
    'tempdata/literature/KDDCup99/KDDCup99_idf.arff',
    'tempdata/literature/Lymphography/Lymphography_withoutdupl_idf.arff',
    'tempdata/literature/PenDigits/PenDigits_withoutdupl_norm_v01.arff',
    'tempdata/literature/Shuttle/Shuttle_withoutdupl_v01.arff',
    'tempdata/literature/Waveform/Waveform_withoutdupl_v01.arff',
    'tempdata/literature/WBC/WBC_v01.arff',
    'tempdata/literature/WDBC/WDBC_withoutdupl_v01.arff',
    'tempdata/literature/WPBC/WPBC_withoutdupl_norm.arff',
    'tempdata/semantic/Annthyroid/Annthyroid_05_v01.arff',
    'tempdata/semantic/Arrhythmia/Arrhythmia_withoutdupl_05_v01.arff',
    'tempdata/semantic/Cardiotocography/Cardiotocography_05_v01.arff',
    'tempdata/semantic/HeartDisease/HeartDisease_withoutdupl_05_v01.arff',
    'tempdata/semantic/Hepatitis/Hepatitis_withoutdupl_05_v01.arff',
    'tempdata/semantic/InternetAds/InternetAds_norm_05_v01.arff',
    'tempdata/semantic/PageBlocks/PageBlocks_05_v01.arff',
    'tempdata/semantic/Parkinson/Parkinson_withoutdupl_05_v01.arff',
    'tempdata/semantic/Pima/Pima_withoutdupl_05_v01.arff',
    'tempdata/semantic/SpamBase/SpamBase_05_v01.arff',
    'tempdata/semantic/Stamps/Stamps_withoutdupl_05_v01.arff',
    'tempdata/semantic/Wilt/Wilt_05.arff',
]

for p in all_paths:
    print(p)
    make_package_for_data(p)



from pathlib import Path
p = Path('outlier_benchmark/datasets')
all = []
for f in p.iterdir():
    name = f.stem
    if name[0] == '_':
        all.append(f'{name[1:].lower()}')
        print(f'from .{name} import {name[1:].lower()}')


print(',\n'.join(all))

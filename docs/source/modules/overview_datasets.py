from dataclasses import asdict
from pathlib import Path

import pandas as pd

import outlier_benchmark.datasets as datasets

l = list()
for i in datasets.__all__:
    if i[0].isupper():
        dataset = getattr(datasets, i)
        l.append(asdict(dataset()))

df_dataset_descriptions = pd.DataFrame(l)
df_dataset_descriptions['name'] = df_dataset_descriptions['name'].apply(lambda name: f':doc:`datasets/{name}`')

"""
Create datasets.rst overview page
"""

template = \
    f"""
..
    !! Do not edit this document directly. Instead, run overview_dataset.py to create it automatically. !!
..

Datasets
========

.. toctree::
    :hidden:
    :glob:

    datasets/*


In total, you have {len(df_dataset_descriptions)} different datasets available. Below, you can find some details. 
Further details may be found in the description of the specific dataset.

{
df_dataset_descriptions.to_markdown(tablefmt="grid", index=False)
}


    ..
        !! Do not edit this document directly. Instead, run overview_dataset.py to create it automatically. !!
    ..

"""

datasets_overview = Path('datasets.rst')

datasets_overview.write_text(template)

"""
Write single page for every dataset
"""

folder = Path('datasets')
folder.mkdir(exist_ok=True)

for dataset in filter(lambda d: d[0].isupper(), datasets.__all__):
    template = \
        f"""
{dataset}
{"=" * len(dataset)}

.. contents::
    :local:

.. autoclass:: outlier_benchmark.datasets.{dataset}
    :members:
    :inherited-members:
"""

    (folder / (dataset + '.rst')).write_text(template)

..  Outlier Benchmark Data documentation master file, created by
    sphinx-quickstart on Wed Jan 20 10:06:28 2021.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

Outlier Benchmark Data
======================

.. raw:: html

   <hr size=10>

A collection of datasets for outlier detection, out-of-distribution detection and unbalanced classification problems.


.. raw:: html

   <hr size=10>

    <div align="center">

    <a href="https://badge.fury.io/py/1"><img src="https://badge.fury.io/py/1.svg" alt="PyPI version" height="18">
    </a>

    <a href='https://outlier-benchmark-data.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/outlier-benchmark-data/badge/?version=latest' alt='Documentation Status' />
    </a>

    <a href="https://codecov.io/gh/JanDiers/outlier-benchmark-data">
        <img src="https://codecov.io/gh/JanDiers/outlier-benchmark-data/branch/master/graph/badge.svg?token=E63CX4Z2BC"/>
    </a>

    <a href="https://www.codefactor.io/repository/github/jandiers/outlier-benchmark-data">
        <img src="https://www.codefactor.io/repository/github/jandiers/outlier-benchmark-data/badge" alt="CodeFactor" />
    </a>
    </div>

   <hr size=10>

This library has the goal to facilitate research in the area of outlier, anomaly and novelty detection as well as related disciplines. The datasets
provided here are taken from the literature of outlier detection and out-of-distribution detection. Currently, we provide 49 datasets that are
widely used in the research community, whereas the number steadily grows.

Starting is easy:

install:
  .. code-block:: sh

    pip install outlier_benchmark_data

import and load data:
   .. code-block:: python

      from outlier_benchmark.datasets import kddcup99
      X, y = kddcup99.load()

See all the datasets in the :doc:`modules/datasets` section.


.. toctree::
   :hidden:
   :maxdepth: 4

   modules/datasets
   modules/dataset_collection
   modules/custom_datasets

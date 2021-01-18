from pathlib import Path

from outlier_benchmark.data.datasets import NEWDataset


def add_to_init(class_name, name, num_samples, num_features, num_outlier, file_path):
    init = Path(
        r'C:\Users\ta46kof\PycharmProjects\outlier-benchmark-data\outlier_benchmark\data\datasets\__init__.py')
    doc = init.read_text()

    template = NEWDataset(name=name, num_samples=num_samples, num_features=num_features, num_outlier=num_outlier,
                          file_path=file_path)
    template = str(template)
    template = class_name + ' = ' + template

    doc += template
    doc += '\n'

    init.write_text(doc)

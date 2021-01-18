from pathlib import Path


def get_template_description(name, lmu_name, n_samples, n_features, n_outlier, class_name, download_link):
    template = Path('./template_description.rst').read_text()
    underline_name = '=' * len(name)
    template = template.format(name=name, lmu_name=lmu_name, underline_name=underline_name,
                               n_samples=n_samples, n_features=n_features,
                               n_outlier=n_outlier, pct_outlier=round(n_outlier / n_samples, 4),
                               class_name=class_name,
                               download_link=download_link)
    return template

from pathlib import Path


def get_list_of_all_files() -> list:
    all = []
    p = Path('./outlier_benchmark/files')
    for d in p.iterdir():
        if 'over sized datasets' not in str(d):
            l = Path(d).iterdir()
            for i in l:
                all.append(i.name)
    return all

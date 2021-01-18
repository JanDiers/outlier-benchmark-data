from .dataset import NEWDataset

Pima20pct = NEWDataset(name='Pima', num_samples=625, num_features=9, num_outlier=125,
                       file_path='../outlier_benchmark/new_files/Pima/20', pct_outlier=0.2)
Lymphography = NEWDataset(name='Lymphography', num_samples=148, num_features=4, num_outlier=6,
                          file_path='../outlier_benchmark/new_files/Lymphography', pct_outlier=0.0405)
Parkinson5pct = NEWDataset(name='Parkinson', num_samples=50, num_features=23, num_outlier=2,
                           file_path='../outlier_benchmark/new_files/Parkinson/5', pct_outlier=0.04)
HeartDisease2pct = NEWDataset(name='HeartDisease', num_samples=153, num_features=14, num_outlier=3,
                              file_path='../outlier_benchmark/new_files/HeartDisease/2', pct_outlier=0.0196)
HeartDisease10pct = NEWDataset(name='HeartDisease', num_samples=166, num_features=14, num_outlier=16,
                               file_path='../outlier_benchmark/new_files/HeartDisease/10', pct_outlier=0.0964)
Pima2pct = NEWDataset(name='Pima', num_samples=510, num_features=9, num_outlier=10,
                      file_path='../outlier_benchmark/new_files/Pima/2', pct_outlier=0.0196)
Pima5pct = NEWDataset(name='Pima', num_samples=526, num_features=9, num_outlier=26,
                      file_path='../outlier_benchmark/new_files/Pima/5', pct_outlier=0.0494)
Hepatitis16pct = NEWDataset(name='Hepatitis', num_samples=80, num_features=20, num_outlier=13,
                            file_path='../outlier_benchmark/new_files/Hepatitis/16', pct_outlier=0.1625)
HeartDisease5pct = NEWDataset(name='HeartDisease', num_samples=157, num_features=14, num_outlier=7,
                              file_path='../outlier_benchmark/new_files/HeartDisease/5', pct_outlier=0.0446)
WBC = NEWDataset(name='WBC', num_samples=454, num_features=10, num_outlier=10,
                 file_path='../outlier_benchmark/new_files/WBC', pct_outlier=0.022)
Pima35pct = NEWDataset(name='Pima', num_samples=768, num_features=9, num_outlier=268,
                       file_path='../outlier_benchmark/new_files/Pima/35', pct_outlier=0.349)
Pima10pct = NEWDataset(name='Pima', num_samples=555, num_features=9, num_outlier=55,
                       file_path='../outlier_benchmark/new_files/Pima/10', pct_outlier=0.0991)
HeartDisease20pct = NEWDataset(name='HeartDisease', num_samples=187, num_features=14, num_outlier=37,
                               file_path='../outlier_benchmark/new_files/HeartDisease/20', pct_outlier=0.1979)
Hepatitis5pct = NEWDataset(name='Hepatitis', num_samples=70, num_features=20, num_outlier=3,
                           file_path='../outlier_benchmark/new_files/Hepatitis/5', pct_outlier=0.0429)
Stamps2pct = NEWDataset(name='Stamps', num_samples=315, num_features=10, num_outlier=6,
                        file_path='../outlier_benchmark/new_files/Stamps/2', pct_outlier=0.019)
WDBC = NEWDataset(name='WDBC', num_samples=367, num_features=31, num_outlier=10,
                  file_path='../outlier_benchmark/new_files/WDBC', pct_outlier=0.0272)
HeartDisease44pct = NEWDataset(name='HeartDisease', num_samples=270, num_features=14, num_outlier=120,
                               file_path='../outlier_benchmark/new_files/HeartDisease/44', pct_outlier=0.4444)
Ionosphere = NEWDataset(name='Ionosphere', num_samples=351, num_features=33, num_outlier=126,
                        file_path='../outlier_benchmark/new_files/Ionosphere', pct_outlier=0.359)
Stamps9pct = NEWDataset(name='Stamps', num_samples=340, num_features=10, num_outlier=31,
                        file_path='../outlier_benchmark/new_files/Stamps/9', pct_outlier=0.0912)
Parkinson75pct = NEWDataset(name='Parkinson', num_samples=195, num_features=23, num_outlier=147,
                            file_path='../outlier_benchmark/new_files/Parkinson/75', pct_outlier=0.7538)
Hepatitis10pct = NEWDataset(name='Hepatitis', num_samples=74, num_features=20, num_outlier=7,
                            file_path='../outlier_benchmark/new_files/Hepatitis/10', pct_outlier=0.0946)
Parkinson20pct = NEWDataset(name='Parkinson', num_samples=60, num_features=23, num_outlier=12,
                            file_path='../outlier_benchmark/new_files/Parkinson/20', pct_outlier=0.2)
Parkinson10pct = NEWDataset(name='Parkinson', num_samples=53, num_features=23, num_outlier=5,
                            file_path='../outlier_benchmark/new_files/Parkinson/10', pct_outlier=0.0943)
Stamps5pct = NEWDataset(name='Stamps', num_samples=325, num_features=10, num_outlier=16,
                        file_path='../outlier_benchmark/new_files/Stamps/5', pct_outlier=0.0492)
Shuttle = NEWDataset(name='Shuttle', num_samples=1013, num_features=10, num_outlier=13,
                     file_path='../outlier_benchmark/new_files/Shuttle', pct_outlier=0.0128)
PenDigits = NEWDataset(name='PenDigits', num_samples=9868, num_features=17, num_outlier=20,
                       file_path='../outlier_benchmark/new_files/PenDigits', pct_outlier=0.002)
WPBC = NEWDataset(name='WPBC', num_samples=198, num_features=34, num_outlier=47,
                  file_path='../outlier_benchmark/new_files/WPBC', pct_outlier=0.2374)

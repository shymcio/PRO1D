import pandas as pd
import numpy as np

names = ['ID', 'Time', 'radius1', 'texture1', 'perimeter1', 'area1', 'smoothness1', 'compactness1', 'concavity1',
         'concave_points1', 'symmetry1', 'fractal_dimension1', 'radius2', 'texture2', 'perimeter2', 'area2',
         'smoothness2', 'compactness2', 'concavity2', 'concave_points2', 'symmetry2', 'fractal_dimension2', 'radius3',
         'texture3', 'perimeter3', 'area3', 'smoothness3', 'compactness3', 'concavity3', 'concave_points3',
         'symmetry3', 'fractal_dimension3', 'tumor_size', 'lymph_node_status', 'Outcome']

data = pd.read_csv('wpbc.csv', header=None, names=names)

data = data.drop(columns=['Time'])
data = data.drop(columns=['ID'])

data['Outcome'] = data['Outcome'].replace('?', np.nan)

data = data.dropna(subset=['Outcome'])

print(data.head(10))

correlation = data.corr()

missing_values = data.isnull().sum()

print("Korelacje:\n", correlation)
print("\nBrakujące wartości:\n", missing_values)



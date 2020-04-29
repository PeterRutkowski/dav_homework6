import pandas as pd
import numpy as np

data = pd.read_csv('data/ans2.tsv', sep='\t')
datasets = np.asarray(data['dataset'])
datasets = np.unique(datasets)

def import_dataset(dataset):
  data = pd.read_csv('data/ans2.tsv', sep='\t')
  x, y = [], []
  for index, row in data.iterrows():
    if row['dataset'] == dataset:
      x.append(row['x'])
      y.append(row['y'])
  return np.asarray(x), np.asarray(y)

for dataset in datasets:
    x, y = import_dataset(dataset)
    prepped_data = np.array([x,y])
    np.save('data/%s.npy'%(str(dataset)), prepped_data)
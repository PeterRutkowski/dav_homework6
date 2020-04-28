import pandas as pd
import numpy as np

def import_data(dataset_label):
    data = pd.read_csv('data/dataset%s.csv' % (str(dataset_label)))
    labels = list(data['country'])
    data = np.asarray(data.drop(['country'], axis=1))
    return data, labels
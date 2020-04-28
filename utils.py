import pandas as pd
import numpy as np

def import_data(dataset_label):
    data = pd.read_csv('ata/dataset%d.csv' % (dataset_label))
    labels = np.asarray(data['country'])
    data = np.asarray(data.drop(['country'], axis=1))
    return data, labels
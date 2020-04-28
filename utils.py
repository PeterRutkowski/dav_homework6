import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from mpld3 import save_html, show

def import_data(dataset_label):
    data = pd.read_csv('data/dataset%s.csv' % (str(dataset_label)))
    labels = list(data['country'])
    data = np.asarray(data.drop(['country'], axis=1))
    return data, labels

def save_plot(filename, fig):
    if len(argv) > 1:
        if argv[1] == '0':
            show(fig)
        else:
            plt.savefig('plots/' + filename + '.png', dpi=200)
            save_html(fig, 'plots/' + filename + '.html')
            print('plots/' + filename + '.png')
            print('plots/' + filename + '.html')
    else:
        plt.savefig('plots/' + filename + '.png', dpi=200)
        save_html(fig, 'plots/' + filename + 'html')
        print('plots/' + filename + '.png')
        print('plots/' + filename + '.html')
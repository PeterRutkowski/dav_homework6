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

def build_plot_dataset_1(data, fig, ax):
    ax.set_ylim(0, 1500000000)
    ax.set_xlim(1960, 2020)
    ax.set_ylabel('Population [billion]')
    ax.set_xlabel('Time')
    ax.set_xticks(np.arange(1960, 2021, 10))
    ax.set_yticks(np.arange(0, 1500000000, 200000000))
    y_labels = ['0', '0.2', '0.4', '0.6', '0.8', '1.0', '1.2', '1.4']
    x_labels = [str(year) for year in np.arange(1960, 2021, 10)]
    ax.set_yticklabels(y_labels)
    ax.set_xticklabels(x_labels)
    ax.set_title('The evolution of populations of most populous countries in 1960')

    years = np.arange(1960, 2019, 1)
    fig.subplots_adjust(right=0.7)
    line_plots = ax.plot(years, data.T, lw=2, alpha=0.8)

    return line_plots

def build_plot_dataset_2(data, fig, ax):
    ax.set_ylim(0, 14000000)
    ax.set_xlim(1960, 2020)
    ax.set_ylabel('Population [million]')
    ax.set_xlabel('Time')
    ax.set_xticks(np.arange(1960, 2021, 10))
    ax.set_yticks(np.arange(0, 14000000, 1500000))
    y_labels = ['0','1.5','3.0','4.5','6.0','7.5','9.0','10.5','12.0','13.5']
    x_labels = [str(year) for year in np.arange(1960, 2021, 10)]
    ax.set_yticklabels(y_labels)
    ax.set_xticklabels(x_labels)
    ax.set_title('The evolution of populations of countries that were most \n' +
              'similar population-wise to Hong Kong in 1984')

    years = np.arange(1960, 2019, 1)
    fig.subplots_adjust(right=0.7)
    line_plots = ax.plot(years, data.T, lw=2, alpha=0.8)

    return line_plots

def save_plot_mpld3(filename, fig):
    if len(argv) > 1:
        if argv[1] == '0':
            show(fig)
        else:
            save_html(fig, 'plots/' + filename + '.html')
            print('plots/' + filename + '.html')
    else:
        save_html(fig, 'plots/' + filename + '.html')
        print('plots/' + filename + '.html')
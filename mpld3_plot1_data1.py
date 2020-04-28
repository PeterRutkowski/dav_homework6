from utils import import_data
from mpld3 import plugins
import mpld3
import numpy as np
import matplotlib.pyplot as plt

data, labels = import_data(1)
years = np.arange(1960,2019,1)

fig, ax = plt.subplots()

ax.set_ylim(0, 1500000000)
ax.set_xlim(1960,2019)
ax.set_ylabel('Population [billion]')
ax.set_xticks(np.arange(1960,2019,5))
ax.set_yticks(np.arange(0,1500000000,200000000))
y_labels = ['0','0.2','0.4','0.6','0.8','1.0','1.2','1.4']
x_labels = [str(year) for year in np.arange(1960,2019,5)]
ax.set_yticklabels(y_labels)
ax.set_xticklabels(x_labels)
ax.set_title('The evolution of populations of most populous countries in 1960')

fig.subplots_adjust(right=0.7)
line_plots = ax.plot(years, data.T, lw=2, alpha=0.8)
interactive_legend = plugins.InteractiveLegendPlugin(line_plots, labels)
plugins.connect(fig, interactive_legend)

plt.tight_layout(2)
mpld3.show()
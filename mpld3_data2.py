from utils import import_data, build_plot_dataset_2, save_plot_mpld3
from mpld3 import plugins
import matplotlib.pyplot as plt

data, labels = import_data(2)

fig, ax = plt.subplots()
plot = build_plot_dataset_2(data, fig, ax)

interactive_legend = plugins.InteractiveLegendPlugin(plot, labels)
plugins.connect(fig, interactive_legend)

save_plot_mpld3('mpld3_data2', fig)
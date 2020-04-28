from utils import import_data, build_plot_dataset_1,save_plot
from mpld3 import plugins
import matplotlib.pyplot as plt

data, labels = import_data(1)

fig, ax = plt.subplots()
plot = build_plot_dataset_1(data, fig, ax)

interactive_legend = plugins.InteractiveLegendPlugin(plot, labels)
plugins.connect(fig, interactive_legend)

save_plot('mpld3_data1', fig)
from bokeh.plotting import figure
from utils import save_bokeh
import numpy as np

data = np.load('data/circle.npy')
x, y = data[0], data[1]

p = figure(title = 'circle')
p.xaxis.axis_label = 'x'
p.yaxis.axis_label = 'y'

p.circle(x, y, fill_alpha=0.2, size=10)

save_bokeh('circle',p)
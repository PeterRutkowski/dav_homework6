from utils import save_plotly
import plotly.express as px
import numpy as np

data = np.load('data/slant_up.npy')
x, y = data[0], data[1]

fig = px.scatter(x=x, y=y)
fig.update_layout(title='slant_up')

save_plotly('slant_up', fig)
from utils import save_plotly
import plotly.express as px
import numpy as np

data = np.load('data/s.npy')
x, y = data[0], data[1]

fig = px.scatter(x=x, y=y)
fig.update_layout(title='s')

save_plotly('s', fig)
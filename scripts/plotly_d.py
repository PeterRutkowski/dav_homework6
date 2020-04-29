from utils import save_plotly
import plotly.express as px
import numpy as np

data = np.load('data/d.npy')
x, y = data[0], data[1]

fig = px.scatter(x=x, y=y, width=600, height=500)
fig.update_layout(title='d')

save_plotly('d', fig)
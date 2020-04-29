from utils import import_data, save_plotly
import plotly.express as px

x, y = import_data(3)

fig = px.scatter(x=x, y=y)

save_plotly('plotly_data3', fig)
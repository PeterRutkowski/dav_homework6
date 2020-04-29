import altair as alt
from utils import save_altair
import numpy as np
import pandas as pd

data = np.load('data/circle.npy')
dict = {'x': data[0], 'y': data[1], 'Dataset': ['circle' for x in data[0]]}
df = pd.DataFrame(dict)

brush = alt.selection(type='interval', resolve='global')

plot = alt.Chart(df).mark_circle().encode(
    x='x',y='y',
    color=alt.condition(brush, 'Dataset:N', alt.value('lightgray'))
    ).add_selection(brush).properties(width=600, height=500)

save_altair('circle', plot)
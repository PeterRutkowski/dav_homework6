import altair as alt
from utils import save_altair
import numpy as np
import pandas as pd

data = np.load('data/bullseye.npy')
dict = {'x': data[0], 'y': data[1], 'Dataset': ['bullseye' for x in data[0]]}
df = pd.DataFrame(dict)

scales = alt.selection_interval(bind='scales')

plot = alt.Chart(df).mark_circle().encode(
    x='x',y='y').add_selection(scales).properties(title='bullseye', width=600, height=500)

save_altair('bullseye', plot)
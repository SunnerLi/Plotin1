from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="darkgrid")

def addValue():
    ax = plt.gca()
    for p in ax.patches:
        x_coordinate = p.get_x() + p.get_width() / 2.
        y_coordinate = p.get_height()
        ax.text(x_coordinate, y_coordinate, int(y_coordinate))

df = pd.read_csv('store.csv')
df = pd.melt(df, id_vars='product', value_name='selling', var_name='year')
sns.factorplot(x='product', y='selling', hue='year', data=df, kind='bar')
addValue()
plt.show()
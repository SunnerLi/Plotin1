from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def addValue():
    ax = plt.gca()
    for p in ax.patches:
        x_coordinate = p.get_x() + p.get_width() / 2.
        y_coordinate = p.get_height()
        value_text = str(y_coordinate)
        ax.text(x_coordinate, y_coordinate, value_text)

# Read data
df = pd.read_csv('life.csv')
df = pd.melt(df, id_vars='country', var_name='sex', value_name='age')
print(df)

# Draw and show
fig = sns.factorplot(x='country', y='age', hue='sex', data=df, kind='bar')
addValue()
plt.show()
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="darkgrid")

def addValue():
    """
        Add value text
        (Verticle)
    """
    ax = plt.gca()
    for p in ax.patches:
        x_coordinate = p.get_x() + p.get_width() / 2.
        y_coordinate = p.get_height()
        ax.text(x_coordinate, y_coordinate, int(y_coordinate))

if __name__ == '__main__':
    df = pd.read_csv('aborigional.csv')
    df = pd.melt(df, id_vars='city', value_name='number', var_name='gender')
    sns.factorplot(x='city', y='number', hue='gender', data=df, kind='bar')
    addValue()
    plt.show()
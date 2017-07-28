from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def addValue():
    """
        Add value text
        (Verticle)
    """
    ax = plt.gca()
    for p in ax.patches:
        x_coor = p.get_x() + p.get_width() / 2.
        y_coor = p.get_height()
        ax.text(x_coor, y_coor, int(y_coor))

if __name__ == '__main__':
    df = pd.read_csv('computer.csv')
    df = pd.melt(df, id_vars='city', value_name='number', var_name='year')
    sns.factorplot(x='city', y='number', hue='year', data=df, kind='bar')
    addValue()
    plt.ylim(0, 300)
    plt.show()
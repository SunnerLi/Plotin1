from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style='darkgrid')

def getZeroBar(color):
    """
        Create a empty bar object which can be the parameter to create the legend

        Arg:    color   - The string of color code
        Ret:    The pyplot Rectangle object
    """
    if color == None:
        exit()
    return plt.bar(0, 0, color=color)

def addValue():
    """
        Add value text
        (Verticle)
    """
    ax = plt.gca()
    for p in ax.patches:
        x_coordinate = p.get_x() + p.get_width() / 2.
        y_coordinate = p.get_height()
        value_text = str(y_coordinate)
        ax.text(x_coordinate, y_coordinate, value_text)

if __name__ == '__main__':
    df = pd.read_csv('garbage.csv')
    sns.barplot(x='year', y='weight', data=df, color='b')
    addValue()
    plt.legend(getZeroBar('b'), ['Weight(g)'])
    plt.show()
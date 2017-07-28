from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="darkgrid")

def addValue(x='x_label', y='y_label', data=None):
    """
        Add the customized value text
        (line chart)
    """
    if type(data) == type(None):
        exit()
    ax = plt.gca()
    x_unit_len = 6. / len(data[x])
    float_rate = (data[y].max() - data[y].min()) / 1000
    for i in range(len(data[x])):
        x_coor = x_unit_len * i
        y_coor = data[y][i] 
        ax.text(x_coor - float_rate * x_unit_len, y_coor * (1 + float_rate), y_coor)

def getZeroBar(color):
    """
        Create a empty bar object which can be the parameter to create the legend

        Arg:    color   - The string of color code
        Ret:    The pyplot Rectangle object
    """
    if color == None:
        exit()
    return plt.bar(0, 0, color=color)

if __name__ == '__main__':
    df = pd.read_csv('height.csv')
    sns.pointplot(x='year', y='height', data=df, color='b')
    addValue(x='year', y='height', data=df)
    plt.legend((getZeroBar('b')), ['Height (cm)'])
    plt.ylim(0, 160)
    plt.show()
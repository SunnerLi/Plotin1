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

if __name__ == '__main__':
    df = pd.read_csv('water.csv')
    sns.pointplot(x='period', y='Degree', data=df, color='b')
    plt.legend((getZeroBar('b'), ), ['Degree'])
    plt.title('The variety image of the water usage in house')
    plt.show()
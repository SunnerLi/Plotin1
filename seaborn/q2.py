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
        x_coordinate = p.get_x() + p.get_width() / 2.
        y_coordinate = p.get_height()
        value_text = str(y_coordinate)
        ax.text(x_coordinate, y_coordinate, value_text)

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
    df = pd.read_csv('feitsui.csv')
    
    # The order cannot be reversed
    sns.barplot(x='year', y='year_total', data=df, color='c')
    sns.barplot(x='year', y='first_half_year', data=df, color='g')
    addValue()
    
    # Customize legend
    plt.legend((getZeroBar('c'), getZeroBar('g')), ['total', 'half'])
    plt.show()
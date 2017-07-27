from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style='darkgrid')

def getZeroBar(color):
    if color == None:
        exit()
    return plt.bar(0, 0, color=color)

def addValue():
    ax = plt.gca()
    for p in ax.patches:
        x_coordinate = p.get_x() + p.get_width() / 2.
        y_coordinate = p.get_height()
        value_text = str(y_coordinate)
        ax.text(x_coordinate, y_coordinate, value_text)

df = pd.read_csv('tourist.csv')
sns.barplot(x='type_of_tourist_amusement', y='value', data=df, color='b')
addValue()
plt.legend(getZeroBar('b'), ['Number'])
plt.show()
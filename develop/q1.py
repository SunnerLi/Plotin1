# barChart1.py

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set(style="darkgrid")

def addValue():
    ax = plt.gca()
    for p in ax.patches:
        x_coordinate = p.get_width()
        y_coordinate = p.get_y() + p.get_height() / 2.
        value_text = str(x_coordinate)
        ax.text(x_coordinate, y_coordinate, value_text)

def getZeroBar(color):
    if color == None:
        exit()
    return plt.bar(0, 0, color=color)

df = pd.read_csv('shop.csv')
sns.barplot(x='selling', y='type_of_tea', data=df, color='b')
addValue()
plt.legend((getZeroBar('b'), ), ['Cups'])
plt.show()
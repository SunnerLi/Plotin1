from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style='darkgrid')

def addValue():
    ax = plt.gca()
    for p in ax.patches:
        x_coor = p.get_width() 
        y_coor = p.get_y() + p.get_height() / 2.
        ax.text(x_coor, y_coor, int(x_coor))

def getZeroBar(color):
    if color == None:
        exit()
    return plt.bar(0, 0, color=color)

df = pd.read_csv('book.csv')
print(df)
sns.barplot(x='loading', y='type_of_book', data=df, color='b')
addValue()
plt.legend((getZeroBar('b'), ), ['Number'])
plt.title('The number')
plt.show()
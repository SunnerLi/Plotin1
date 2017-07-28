from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="darkgrid")

def getZeroBar(color):
    if color == None:
        exit()
    return plt.bar(0, 0, color=color)

df = pd.read_csv('weight.csv')
sns.pointplot(x='id', y='weight', data=df, color='b')
plt.legend(getZeroBar('b'), ['Weight (kg)'])
plt.ylim(24, 28)
plt.show()
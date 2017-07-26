from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import seaborn as sns
import numpy as np

sns.set(style="darkgrid")

class PlotIn1(object):
    def __init__(self):
        pass

    def factorplot(self, x='x_name', y='y_name', hue='label_name', data=None, kind='bar'):
        df = pd.melt(data, id_vars=x, var_name=hue, value_name=y)
        fig = sns.factorplot(x=x, y=y, hue=hue, data=df, kind=kind, legend=False, legend_out=True)
        plt.legend(loc=1)

        # Add value text in bar chart
        ax = plt.gca()
        if len(ax.patches) != 0:
            for p in ax.patches:
                x_coor = p.get_x() + p.get_width() / 2.
                y_coor = p.get_height()
                ax.text(x_coor, y_coor, y_coor, ha='center', va='bottom')

        # Add value text in line chart
        else:
            x_unit_len = 6. / len(data[x])
            float_rate = (data[y].max() - data[y].min()) / 500
            for i in range(len(data[x])):
                x_coor = x_unit_len * i
                y_coor = data[y][i] 
                ax.text(x_coor, y_coor * (1 + float_rate), y_coor, ha='center', va='bottom')


df = pd.read_csv('weight.csv')
pi1 = PlotIn1()

# 1
#pi1.factorplot('country', 'age', 'sex', df, kind='bar')

# 2
#sns.barplot(x='selling', y='type_of_tea', data=df, color='green')

# 3
pi1.factorplot(x='id', y='weight', data=df, kind="point")

# 4
#sns.lmplot(x='x', y='y', data=df, fit_reg=False, hue='class')


plt.show()
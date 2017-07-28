from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="darkgrid")

if __name__ == '__main__':
    df = pd.read_csv('grade.csv')
    df.columns = ['subject', 'Pass (over 60)', 'Fail']
    df = pd.melt(df, id_vars='subject', value_name='people', var_name='fail_or_not')
    sns.factorplot(x='people', y='subject', hue='fail_or_not', data=df, kind='bar')
    plt.show()
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

color = ['green', 'blue', 'red']

def BarChart(xTag, y, labels):
    style.use('ggplot')
    print style.available
    x = np.arange(len(xTag))

    # Looping plot
    width = 0.3
    bar = [None] * 2
    for i in xrange(len(y)):
        initPos = -(len(y)-1)*0.5
        currPos = initPos + i
        if i < 1 or i > 3:
            bar[i] = plt.bar(x + currPos*width, y[i], width=width, 
                align='center', alpha=0.8, label=labels[i])
        else:
            bar[i] = plt.bar(x + currPos*width, y[i], width=width, 
                align='center', alpha=0.8, label=labels[i], color=color[i-1])
        for a, b in zip(x, y[i]):
            plt.text(a + currPos*width, b, str(b))

    plt.ylim(50, 80)
    plt.xticks(x, xTag)
    plt.legend()
    plt.plot()
    return plt

def BarChart_ylim(_plt, a, b):
    _plt.ylim(a, b)
    return _plt
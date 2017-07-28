from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

def plot():
    x = np.arange(0, 100, 0.1)
    y1 = 10 -x
    y2 = 10000 * x
    yAxis = 0 * len(x)
    plt.plot(x, y1)
    plt.fill_between(x, y1, color='red', alpha='0.2')
    plt.fill_between(x, y1, y2, color='blue', alpha='0.2')
    plt.ylim(0, 10)
    plt.xlim(0, 10)
    plt.show()


plot()
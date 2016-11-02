from matplotlib import pyplot as plt
from simpleChart import *

x = [87, 88, 89, 90, 91]
y = [[1877, 1115, 1832, 1842, 731], [3860, 1772, 3368, 3229, 1781]]
labels = ['Second half year', 'First half year']

if __name__ == "__main__":
    plt = BarStackChart(x, y, labels)
    plt.show()
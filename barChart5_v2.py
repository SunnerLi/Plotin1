from matplotlib import pyplot as plt
from simpleChart import *

x = [85, 86, 87, 88, 89, 90]
y = [1140, 1140, 1140, 1080, 980, 890]

if __name__ == "__main__":
    plt = BarChart(x, y, ["Weight (g)"])
    plt.show()
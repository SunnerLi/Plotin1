from matplotlib import pyplot as plt
from simpleChart import *

x = [3, 4, 5, 6, 7, 8]
y = [25, 26.5, 27, 26.5, 26, 25.5]

if __name__ == "__main__":
    plt = LineChart(x, y, ["Weight (kg)"])
    plt.savefig('lineChart1.jpg')
    #plt.show()
from matplotlib import pyplot as plt
from simpleChart import *

x = ['Taipei', 'Ilan', 'Taoyuan', 'Hsinchu']
y = [[16505, 6704, 20296, 8434], [17757, 6363, 20922, 7947]]

if __name__ == "__main__":
    plt = BarChart(x, y, ["Male", "Female"])
    plt.show()
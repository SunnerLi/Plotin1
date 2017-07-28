from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = ['Taipei', 'Ilan', 'Taoyuan', 'Hsinchu']
y = [[16505, 6704, 20296, 8434], [17757, 6363, 20922, 7947]]

if __name__ == "__main__":
    plt = pi1.BarChart(x, y, ["Male", "Female"])
    plt.show()
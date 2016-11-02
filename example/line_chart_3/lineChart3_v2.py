from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = [0, 2, 4, 6, 8, 10, 12, 14]
y = [45, 85, 105, 120, 125, 130]

if __name__ == "__main__":
    plt = LineChart(x, y, ["Height (cm)"])
    plt.show()
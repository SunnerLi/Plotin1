from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = [3, 4, 5, 6, 7, 8]
y = [25, 26.5, 27, 26.5, 26, 25.5]

if __name__ == "__main__":
    plt = LineChart(x, y, ["Weight (kg)"])
    plt.show()
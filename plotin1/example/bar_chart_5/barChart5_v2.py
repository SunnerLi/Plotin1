from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = [85, 86, 87, 88, 89, 90]
y = [1140, 1140, 1140, 1080, 980, 890]

if __name__ == "__main__":
    plt = BarChart(x, y, ["Weight (g)"])
    plt.show()
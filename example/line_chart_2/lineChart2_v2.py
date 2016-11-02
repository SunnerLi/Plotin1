from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = ['1-2', '3-4', '5-6', '7-8', '9-10', '11-12']
y = [84, 86, 88, 93, 86, 82]

if __name__ == "__main__":
    plt = LineChart(x, y, ["Degree"])
    plt.show()
from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = ['Math', 'Science']
y = [[11, 16], [13, 8]]

if __name__ == "__main__":
    plt = BarhChart(x, y, ["Pass (over 60)", "Fail"])
    plt.show()
from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


# Data declare
x = ['ROC', 'Japan', 'English', 'America', 'Singapore',
        'Korea', 'Philippines']
y = [[72, 77, 74, 74, 75, 70, 66], [78, 80, 80, 79, 79, 77, 69]]

if __name__ == "__main__":
    plt = BarChart(x, y, ["Male", "Female"])
    plt.show()
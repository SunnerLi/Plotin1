from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = ['The 6th selection area', 'The 5th selection area', 'The 4th selection area',
        'The 3rd selection area', 'The 2nd selection area', 'The 1st selection area']
y = [[5, 2, 2, 2, 2, 4], [6, 5, 5, 7, 5, 6]]

if __name__ == "__main__":
    plt = BarhStackChart(x, y, ["Male", "Female"])
    plt.show()
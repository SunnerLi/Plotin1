from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1, 10])
y = np.array([10, 9, 8, 7, 6, 5, 4, 2, 2, 1])
tag = np.array([1, 1, 1, 1, 1, -1, -1, -1, -1, -1])

if __name__ == "__main__":
    plt = PointChart(x, y, tag)

    # Draw the region
    x = np.arange(0, 20, 0.1)
    y1 = 9.5 - 0.8 * x
    y2 = 1000 * x
    yAxis = 0 * len(x)
    plt.plot(x, y1)
    plt.fill_between(x, y1, color='blue', alpha='0.2')
    plt.fill_between(x, y1, y2, color='red', alpha='0.2')

    # Limit the scale
    plt.ylim(0, 11)
    plt.xlim(0, 11)
    plt.show()
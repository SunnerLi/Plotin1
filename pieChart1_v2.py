from matplotlib import pyplot as plt
from simpleChart import *

y = np.array([5000, 2500, 5830, 6670])
x = ['Buy book', 'Deposit', 'Pocket money', 'Buy the model']

if __name__ == "__main__":
    plt = PieChart(x, y)
    plt.show()
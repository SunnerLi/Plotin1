from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = ['Air cleaner', 'Dehumidifier', 'Fan', 'Air conditioner']
y = [31, 56, 110, 77]

if __name__ == "__main__":
    plt = PieChart(x, y)
    plt.show()
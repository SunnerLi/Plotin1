from matplotlib import pyplot as plt
from simpleChart import *

x = ['Air cleaner', 'Dehumidifier', 'Fan', 'Air conditioner']
y = [31, 56, 110, 77]

if __name__ == "__main__":
    plt = PieChart(x, y)
    plt.savefig('pieChart2.jpg')
    #plt.show()
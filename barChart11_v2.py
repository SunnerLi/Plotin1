from matplotlib import pyplot as plt
from simpleChart import *

x = ['Shampoo', 'Body wash', 'Perfume', 'Towel']
y = [[27000, 30000, 36000, 19000], [24000, 34000, 42000, 19000]]

if __name__ == "__main__":
    plt = BarChart(x, y, ["Year 88", "Year 89"])
    plt.show()
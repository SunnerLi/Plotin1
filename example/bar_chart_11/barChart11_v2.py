from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = ['Shampoo', 'Body wash', 'Perfume', 'Towel']
y = [[27000, 30000, 36000, 19000], [24000, 34000, 42000, 19000]]

if __name__ == "__main__":
    plt = pi1.BarChart(x, y, ["Year 88", "Year 89"])
    plt.show()
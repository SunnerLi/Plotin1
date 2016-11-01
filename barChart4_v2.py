from matplotlib import pyplot as plt
from simpleChart import *

x = ['National\npark', 'Beach', 'National\nscenic\narea', 
        'Leisural\nagricultural\narea', 'Forest\nrecreation\narea',
        'Golf\nfield', 'Amusement\npark', 'Spring', 'Monument']
y = np.array([[6, 49, 9, 20, 20, 83, 71, 103, 379]])

if __name__ == "__main__":
    plt = BarChart(x, y, ["Number"])
    plt = BarChart_ylim(plt, 0, 400)
    plt.show()

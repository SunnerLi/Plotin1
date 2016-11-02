from matplotlib import pyplot as plt
from plotin1 import *

# Data declare
x = ['Buring\nxiancao', 'Hot\norange\ntea', 'Hot\nred\nbean\nsoup',  
        'Coffee\nsmoothies', 'Cold\nmilk\ntea']
y = [280, 200, 320, 120, 180]

if __name__ == "__main__":
    plt = BarhChart(x, y, ["Cups"])
    plt.savefig('barChart1.jpg')
    #plt.show()
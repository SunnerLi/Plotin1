from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1

# Data declare
x = ['Buring\nxiancao', 'Hot\norange\ntea', 'Hot\nred\nbean\nsoup',  
        'Coffee\nsmoothies', 'Cold\nmilk\ntea']
y = [280, 200, 320, 120, 180]

if __name__ == "__main__":
    plt = pi1.BarhChart(x, y, ["Cups"])
    #plt.savefig('barChart1.jpg')
    plt.show()
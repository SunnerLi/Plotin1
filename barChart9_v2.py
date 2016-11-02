from matplotlib import pyplot as plt
from simpleChart import *

x = ['Math', 'Science']
y = [[11, 16], [13, 8]]

if __name__ == "__main__":
    plt = BarhChart(x, y, ["Pass (over 60)", "Fail"])
    plt.savefig('barChart9.jpg')
    #plt.show()
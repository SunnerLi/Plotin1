from matplotlib import pyplot as plt
from simpleChart import *

x= ['Others', 'Picture\nbook', 'Science\necyclopedia', 
        'Children\nmegazine', 'People\nmegazine']
y = [439, 457, 358, 415, 365]

if __name__ == "__main__":
    plt = BarhChart(x, y, ['Number'])
    plt.show()

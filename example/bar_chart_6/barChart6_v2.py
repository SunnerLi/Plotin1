from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x= ['Others', 'Picture\nbook', 'Science\necyclopedia', 
        'Children\nmegazine', 'People\nmegazine']
y = [439, 457, 358, 415, 365]

if __name__ == "__main__":
    plt = BarhChart(x, y, ['Number'])
    plt.show()

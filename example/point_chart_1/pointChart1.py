from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

# Color
color = ['green', 'blue', 'yellow', 'red']

def plot(_plt):
    x = np.arange(0, 100, 0.1)
    y1 = 20 -x
    y2 = 10000 * x
    yAxis = 0 * len(x)
    _plt.plot(x, y1)
    _plt.fill_between(x, y1, color='blue', alpha='0.2')
    _plt.fill_between(x, y1, y2, color='red', alpha='0.2')
    _plt.ylim(0, 20)
    _plt.xlim(0, 20)
    _plt.show()


def generation():
    global x
    global y
    global tag
    N = 50
    x = np.concatenate((np.random.random(N) * 10, (np.random.random(N) * 10 + 10)))
    y = np.concatenate((np.random.random(N) * 10, (np.random.random(N) * 10 + 10)))
    tag = np.array(np.sign(x+y-20))

# Get the data
x = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1, 10])
y = np.array([10, 9, 8, 7, 6, 5, 4, 2, 2, 1])
tag = np.array([1, 1, 1, 1, 1, -1, -1, -1, -1, -1])
generation()

# Count the number of tag
tagSet = set()
for t in tag:
    if not t in tagSet:
        tagSet.add(t)

colorCount = 0
for key in tagSet:
    # Count the subset points of each type
    _x = []
    _y = []
    for i in range(len(x)):
        if tag[i] == key:
            _x.append(x[i])
            _y.append(y[i])
    if colorCount < 1 or colorCount > len(color):
        plt.plot(_x, _y, 'o')
    else:
        plt.plot(_x, _y, 'o', color=color[colorCount])
        colorCount += 1

plot(plt)

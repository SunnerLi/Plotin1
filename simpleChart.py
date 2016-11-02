from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

color = ['green', 'blue', 'red']

def BarChart(xTag, _y, labels):
    # Revise the dimension of y
    y = np.array(_y)
    if len(np.shape(y)) < 2:
        y = np.array([_y])
    y = y.tolist()

    # Shift for x-axis
    xTag, y = __BarChart_shift(xTag, y)
    x = np.arange(len(xTag))    

    # Looping plot
    width = 0.3
    bar = [None] * 2
    for i in xrange(len(y)):
        initPos = -(len(y)-1)*0.5
        currPos = initPos + i
        if i < 1 or i > len(color):
            bar[i] = plt.bar(x + currPos*width, y[i], width=width, 
                align='center', alpha=0.8, label=labels[i])
        else:
            bar[i] = plt.bar(x + currPos*width, y[i], width=width, 
                align='center', alpha=0.8, label=labels[i], color=color[i-1])

        # Print the value tag
        for a, b in zip(x, y[i]):
            if not b == 0:
                plt.text(a + currPos*width, b, str(b))

    plt.xticks(x, xTag)
    plt.legend()
    plt.plot()
    return plt

def __BarChart_shift(x, y):
    # Initial
    _x = [' ']
    _y = []
    for i in xrange(len(y)):
        _y.append([])

    # Append
    _x = _x + x + _x
    for i in range(len(y)):
        _y[i] = [0] + y[i] + [0]
    return _x, np.array(_y) 

def BarChart_ylim(_plt, a, b):
    _plt.ylim(a, b)
    return _plt


def BarhChart(xTag, _y, labels):
    # Revise the dimension of y
    y = np.array(_y)
    if len(np.shape(y)) < 2:
        y = np.array([_y])
    y = y.tolist()

    # Shift for x-axis
    xTag, y = __BarChart_shift(xTag, y)
    x = np.arange(len(xTag))    

    # Looping plot
    height = 0.3
    bar = [None] * 2
    for i in xrange(len(y)):
        initPos = -(len(y)-1)*0.5
        currPos = initPos + i
        if i < 1 or i > len(color):
            bar[i] = plt.barh(x + currPos*height, y[i], height=height, 
                align='center', alpha=0.8, label=labels[i])
        else:
            bar[i] = plt.barh(x + currPos*height, y[i], height=height, 
                align='center', alpha=0.8, label=labels[i], color=color[i-1])

        # Print the value tag
        for a, b in zip(x, y[i]):
            if not b == 0:
                plt.text(a + currPos*height, b, str(b))

    plt.yticks(x, xTag)
    plt.legend()
    plt.plot()
    return plt

def BarStackChart(xTag, _y, labels):
    # Revise the dimension of y
    y = np.array(_y)
    if len(np.shape(y)) < 2:
        y = np.array([_y])
    y = y.tolist()

    # Shift for x-axis
    xTag, y = __BarChart_shift(xTag, y)
    x = np.arange(len(xTag))    

    # Looping plot
    width = 0.3
    bar = [None] * 2
    for i in xrange(len(y)-1, -1, -1):
        initPos = -(len(y)-1)*0.5
        currPos = initPos + i
        if i < 1:
            print 'default color'
            bar[i] = plt.bar(x, y[i], width=width, align='center', 
                alpha=0.7, label=labels[i])
        elif i > len(color):
            bar[i] = plt.bar(x, y[i] + y[i-1], width=width, align='center', 
                alpha=0.7, label=labels[i])
        else:
            bar[i] = plt.bar(x, y[i] + y[i-1], width=width, align='center', 
                alpha=0.7, label=labels[i], color=color[i-1])

        # Print the value tag
        for a, b in zip(x, y[i]):
            if not b == 0:
                if i < 1:
                    plt.text(a, b, str(b))
                else:
                    for c, d in zip(x, y[i-1]):
                        if not b == 0 and a == c:
                            plt.text(a, b + d, str(b))

    plt.xticks(x, xTag)
    plt.legend()
    plt.plot()
    return plt

def LineChart(xTag, _y, labels):
    # Revise the dimension of y
    y = np.array(_y)
    if len(np.shape(y)) < 2:
        y = np.array([_y])
    y = y.tolist()
    x = np.arange(len(xTag))

    # Draw the line
    for i in xrange(len(y)):
        line = plt.plot(x, y[i], 'o-', label="Weight (kg)")
        for a, b in zip(x, y[i]):
            if not b == 0:
                plt.text(a, b, str(b))

    # Revise the range of y-axis
    minNum = y[0][0]
    maxNum = y[0][0]
    for i in range(len(y)):
        if np.min(y[i]) < minNum:
            minNum = np.min(y[i])
        if np.max(y[i]) > maxNum:
            maxNum = np.max(y[i])
    std = np.std(y)

    plt.xticks(x, xTag)
    plt.ylim(minNum - std, maxNum + std)
    plt.legend()
    plt.plot()
    return plt
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.arange(2)
y = np.array([[11, 16], [13, 8]])
xTag = ['Math', 'Science']

height = 0.2
bar1 = plt.barh(x+height/2, y[0], height=height, align='center')
for a, b in zip(x, y[0]):
    plt.text(b, a+height/2, str(b))
bar2 = plt.barh(x-height/2, y[1], height=height, align='center', color='green')
for a, b in zip(x, y[1]):
    plt.text(b, a-height/2, str(b))

plt.yticks(x, xTag)
plt.legend((bar1, bar2), ("Pass (over 60)", "Fail"))
plt.plot()
plt.show()
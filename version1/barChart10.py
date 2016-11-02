from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.arange(4)
xTag = ['Taipei', 'Ilan', 'Taoyuan', 'Hsinchu']
y = np.array([[16505, 6704, 20296, 8434], [17757, 6363, 20922, 7947]])

width = 0.2
bar1 = plt.bar(x-width/2, y[0], width=width, align='center', alpha=0.7, label="Male")
for a, b in zip(x, y[0]):
    plt.text(a-width, b, str(b))
bar2 = plt.bar(x+width/2, y[1], width=width, align='center', alpha=0.7, label="Female", color='yellow')
for a, b in zip(x, y[1]):
    plt.text(a, b, str(b))

plt.xticks(x, xTag)
plt.legend()
plt.plot()
plt.show()
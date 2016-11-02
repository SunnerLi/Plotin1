# http://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x = np.arange(7)
xTag = ['ROC', 'Japan', 'English', 'America', 'Singapore',
        'Korea', 'Philippines']
y1 = np.array([72, 77, 74, 74, 75, 70, 66])
y2 = np.array([78, 80, 80, 79, 79, 77, 69])

bar_width = 0.2
style.use('ggplot')
bar1 = plt.bar(x-bar_width/2, y1, width=bar_width, alpha=0.8, align='center', color="green")
for a, b in zip(x, y1):
    plt.text(a-bar_width, b, str(b))


bar2 = plt.bar(x+bar_width/2, y2, width=bar_width, alpha=0.8, align='center')
for a, b in zip(x, y2):
    plt.text(a, b, str(b))

plt.set_position()
plt.legend((bar1, bar2), ("Male", "Female"), loc='lower center')
plt.ylim(50, 80)
plt.plot()
plt.show()
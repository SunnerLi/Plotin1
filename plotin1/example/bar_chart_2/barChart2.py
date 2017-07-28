from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x = np.array([87, 88, 89, 90, 91])
y1 = np.array([1877, 1115, 1832, 1842, 731])
y2 = np.array([3860, 1772, 3368, 3229, 1781])
bar_width = 0.5

style.use('ggplot')
bar1 = plt.bar(x, y1, align='center', alpha=0.8, width=bar_width)
for a, b in zip(x, y1):
    plt.text(a - bar_width/3, b, str(b))

bar2 = plt.bar(x, y2, align='center', alpha=0.8, width=bar_width)
for a, b in zip(x - bar_width/3, y2):
    plt.text(a, b, str(b))

plt.legend((bar1, bar2), ("Second half year", "First half year"))
plt.plot()
plt.show()
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = xrange(6)
xTag = ['The 6th selection area', 'The 5th selection area', 'The 4th selection area',
        'The 3rd selection area', 'The 2nd selection area', 'The 1st selection area']
y = np.array([[5, 2, 2, 2, 2, 4], [6, 5, 5, 7, 5, 6]])

bar2 = plt.barh(x, y[1]+y[0], align='center', alpha=0.7, label="Female", color='green')
for a, b, c in zip(x, y[1], y[0]):
    plt.text(b + c, a, str(b))
bar1 = plt.barh(x, y[0], align='center', alpha=0.7, label="Male")
for a, b in zip(x, y[0]):
    plt.text(b, a, str(b))

plt.yticks(x, xTag)
plt.legend()
plt.plot()
plt.show()
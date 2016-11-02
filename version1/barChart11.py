from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.arange(4)
xTag = ['Shampoo', 'Body wash', 'Perfume', 'Towel']
y = np.array([[27000, 30000, 36000, 19000], [24000, 34000, 42000, 19000]])

width = 0.2
bar1 = plt.bar(x-width/2, y[0], width=width, align='center', alpha=0.7, label="Year 88", color='green')
for a, b in zip(x, y[0]):
    plt.text(a-width, b, str(b))
bar2 = plt.bar(x+width/2, y[1], width=width, align='center', alpha=0.7, label="Year 89", color='red')
for a, b in zip(x, y[1]):
    plt.text(a, b, str(b))

plt.xticks(x, xTag)
plt.legend()
plt.plot()
plt.show()
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.arange(6)
xTag = ['1-2', '3-4', '5-6', '7-8', '9-10', '11-12']
y = np.array([84, 86, 88, 93, 86, 82])

plt.plot(x, y, 'o-', alpha=0.8, label="Degree")
for a, b in zip(x, y):
    plt.text(a, b, str(b))

plt.ylim(np.min(y) - np.std(y), np.max(y) + np.std(y))
plt.title("The variety image of the water usage in house")
plt.legend()
plt.xticks(x, xTag)
plt.plot()
plt.show()
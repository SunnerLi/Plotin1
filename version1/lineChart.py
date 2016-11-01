from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([25, 26.5, 27, 26.5, 26, 25.5])

style.use('ggplot')
line = plt.plot(x, y, 'o-', label="Weight (kg)")
plt.ylim(24, 28)
plt.legend()
plt.show()
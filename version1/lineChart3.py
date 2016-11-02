from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.array([0, 2, 4, 6, 8, 10, 12, 14])
y = np.array([45, 85, 105, 120, 125, 130])

if not len(x) == len(y):
    plt.xlim(x[0], x[-1])
    xRev = x.tolist()
    x = xRev[:len(xRev)-2]
    x = np.array(x)

batch = plt.plot(x, y, 'o-', alpha=0.7)
for a, b in zip(x, y):
    plt.text(a, b, str(b))

plt.legend(batch, ("Height (cm)",))
plt.show()
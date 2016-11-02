from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.array([85, 86, 87, 88, 89, 90])
y = np.array([1140, 1140, 1140, 1080, 980, 890])

bar = plt.bar(x, y, align='center', width=0.5, alpha=0.8, label='Weight (g)')
for a, b in zip(x, y):
    plt.text(a, b, str(b))
plt.legend()
plt.plot()
plt.show()
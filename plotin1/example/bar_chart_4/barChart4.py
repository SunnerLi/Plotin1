from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x = np.arange(11)
y = np.array([0, 6, 49, 9, 20, 20, 83, 71, 103, 379, 0])
xTag = ['', 'National\npark', 'Beach', 'National\nscenic\narea', 
        'Leisural\nagricultural\narea', 'Forest\nrecreation\narea',
        'Golf\nfield', 'Amusement\npark', 'Spring', 'Monument', '']

style.use('ggplot')
bar = plt.bar(x, y, align='center', width=0.5, alpha=0.8, label="Number", color='green')
for a, b in zip(x, y):
    if not b == 0:
        plt.text(a, b, str(b))

plt.xticks(x, xTag)
plt.legend()
plt.plot()
plt.show()
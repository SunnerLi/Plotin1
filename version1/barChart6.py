from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.arange(5)
y = np.array([439, 457, 358, 415, 365])
xTag = ['Others', 'Picture\nbook', 'Science\necyclopedia', 
        'Children\nmegazine', 'People\nmegazine']

bar = plt.barh(x, y, align='center', alpha=0.5, label='Number', color='red')
for a, b in zip(y, x):
    plt.text(a, b, str(a))

plt.yticks(x, xTag)
plt.plot()
plt.show()
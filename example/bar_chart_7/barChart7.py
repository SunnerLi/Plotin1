from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

x = np.arange(7)
y = np.array([[195, 152, 129, 178, 167, 122, 145], 
                [240, 176, 150, 230, 208, 165, 157]])
xTag = ['Taipei', 'Kaohsiung', 'Keelung', 'Hsinchu', 'Taichung', 
        'Chiayi', 'Tainan']
labels = ['Year 89', 'Year 90']

# Looping plot
width = 0.3
bar = [None] * 2
for i in xrange(len(y)):
    initPos = -(len(y)-1)*0.5
    currPos = initPos + i
    bar[i] = plt.bar(x + currPos*width, y[i], width=width, align='center', alpha=0.8, label=labels[i])
    for a, b in zip(x, y[i]):
        plt.text(a + currPos*width, b, str(b))

plt.ylim(0, 300)
plt.xticks(x, xTag)
plt.legend()
plt.plot()
plt.show()

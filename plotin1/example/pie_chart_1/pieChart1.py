from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

# Define the data
values = np.array([5000, 2500, 5830, 6670])
labels = ['Buy book', 'Deposit', 'Pocket money', 'Buy the model']
colors = ['green', 'blue', 'red', 'yellow']

# Plot
style.use('ggplot')
ax = plt.subplot()
patch, text, _ = ax.pie(values, labels=labels, colors=colors, autopct=make_autopct(values))

ax.legend(patch, labels)
ax.plot()
plt.show()
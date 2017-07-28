from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

def __autopct(value):
    def _autopct(pct):
        total = sum(value)
        val = int(round(pct*total/100))
        return str(val)
    return _autopct

x = ['Air cleaner', 'Dehumidifier', 'Fan', 'Air conditioner']
y = [31, 56, 110, 77]
color = ['blue', 'red', 'yellow', 'green']

batch, text, _ = plt.pie(y, labels=x, colors=color, autopct=__autopct(y))
plt.legend(batch, x)
plt.plot()
plt.show()
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# Data declare
x = ['Buring xiancao', 'Hot orange tea', 'Hot red bean soup',  
        'Coffee smoothies', 'Cold milk tea']
y = np.array([280, 200, 320, 120, 180])
xNum = np.arange(len(x))

#plt.rcdefaults()
style.use('ggplot')
bar = plt.barh(xNum, y, align='center', alpha=0.8, height=0.5)
plt.yticks(xNum, x)
plt.legend((bar,), ("Cups",))
plt.plot()
plt.show()















































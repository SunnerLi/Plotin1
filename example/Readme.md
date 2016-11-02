# Example Directory
The following shows each type of the chart. You can check which type you want to use. The code is given at below.    
<br/>
You should import the package first. Since plotin1 is a wrapper of matplotlib, matplotlib needs to be imported if you want to show the image or other advance operation.    
```python
import matplotlib.pyplot as plt
import plotin1 as pi1
...
```
<br/>
<br/>
## Content
```
* <file_name>_v2.py: The program that use plotin1 to draw the chart
* <file_name>.py: The program that use numpy and matplotlib to draw
```
<br/>
<br/>
## Bar Chart
<p align="left">
  <img src="https://github.com/SunnerLi/chart/blob/master/img/barChart3.jpg"/>
</p>
```python
x = ['ROC', 'Japan', 'English', 'America', 'Singapore', 'Korea', 'Philippines']
y = [[72, 77, 74, 74, 75, 70, 66], [78, 80, 80, 79, 79, 77, 69]]

if __name__ == "__main__":
    plt = pi1.BarChart(x, y, ["Male", "Female"])
    plt.show()
```
<br/>
## Bar Stack Chart
<p align="left">
  <img src="https://github.com/SunnerLi/chart/blob/master/img/barChart2.jpg"/>
</p>
```python
x = [87, 88, 89, 90, 91]
y = [[1877, 1115, 1832, 1842, 731], [3860, 1772, 3368, 3229, 1781]]
labels = ['Second half year', 'First half year']

if __name__ == "__main__":
    plt = pi1.BarStackChart(x, y, labels)
    plt.show()
```
<br/>
## Bar Horizontal Chart
<p align="left">
  <img src="https://github.com/SunnerLi/chart/blob/master/img/barChart1.jpg"/>
</p>
```python
x = ['Buring\nxiancao', 'Hot\norange\ntea', 'Hot\nred\nbean\nsoup', 'Coffee\nsmoothies', 'Cold\nmilk\ntea']
y = [280, 200, 320, 120, 180]

if __name__ == "__main__":
    plt = pi1.BarhChart(x, y, ["Cups"])
    plt.show()
```
<br/>
## Bar Horizontal Stack Chart
<p align="left">
  <img src="https://github.com/SunnerLi/chart/blob/master/img/barChart8.jpg"/>
</p>
```python
x = ['The 6th selection area', 'The 5th selection area', 'The 4th selection area',
        'The 3rd selection area', 'The 2nd selection area', 'The 1st selection area']
y = [[5, 2, 2, 2, 2, 4], [6, 5, 5, 7, 5, 6]]

if __name__ == "__main__":
    plt = pi1.BarhStackChart(x, y, ["Male", "Female"])
    plt.show()
```
<br/>
## Line Chart
<p align="left">
  <img src="https://github.com/SunnerLi/chart/blob/master/img/lineChart1.jpg"/>
</p>
```python
x = [3, 4, 5, 6, 7, 8]
y = [25, 26.5, 27, 26.5, 26, 25.5]

if __name__ == "__main__":
    plt = pi1.LineChart(x, y, ["Weight (kg)"])
    plt.show()
```
<br/>
## Pie Chart
<p align="left">
  <img src="https://github.com/SunnerLi/chart/blob/master/img/pieChart1.jpg"/>
</p>
```python
y = np.array([5000, 2500, 5830, 6670])
x = ['Buy book', 'Deposit', 'Pocket money', 'Buy the model']

if __name__ == "__main__":
    plt = pi1.PieChart(x, y)
    plt.show()
```
<br/>
## Point Chart
<p align="left">
  <img src="https://github.com/SunnerLi/chart/blob/master/img/pointChart2.jpg"/>
</p>
The implementations of point chart is a little complicated, so you should see the code directly for more detail.     
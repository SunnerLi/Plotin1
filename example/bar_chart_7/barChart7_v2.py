from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


x = ['Taipei', 'Kaohsiung', 'Keelung', 'Hsinchu', 'Taichung', 
        'Chiayi', 'Tainan']
y = np.array([[195, 152, 129, 178, 167, 122, 145], 
                [240, 176, 150, 230, 208, 165, 157]])

if __name__ == "__main__":
    plt = BarhChart(x, y, ['Year 89', 'Year 90'])
    plt.show()
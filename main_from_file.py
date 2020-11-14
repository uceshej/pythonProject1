
import matplotlib.pyplot as plt
from plotter import Plotter
plotter = Plotter()
def plot_point():
    with open('input.csv','r') as f:
        plot1=f.readlines()[1:]
        point_x_all=[]
        point_y_all=[]
        draw_point=()
        for row1 in plot1:
            each_rows1=row1.strip('\n')
            each_row1=each_rows1.split(',')
            point_id=each_row1[0]
            point_x=each_row1[1]
            point_y=each_row1[2]
            point_x_all.append(float(point_x))
            point_y_all.append(float(point_y))
        plotter.add_point(point_x_all, point_y_all, )

def plot_polygon():
    with open('polygon.csv','r') as f:
        plot=f.readlines()[1:]
        polygon_x_all=[]
        polygon_y_all=[]
        draw_polygon=()
        for row in plot:
            each_rows=row.strip('\n')
            each_row=each_rows.split(',')
            polygon_id=each_row[0]
            polygon_x=each_row[1]
            polygon_y=each_row[2]
            polygon_x_all.append(int(polygon_x))
            polygon_y_all.append(int(polygon_y))
        plotter.add_polygon(list(polygon_x_all), list(polygon_y_all))

plot_point()
plot_polygon()
plt.show()



from plotter import Plotter
import matplotlib.pyplot as plt
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
    draw_polygon=(polygon_x_all,polygon_y_all)
    list1=list(draw_polygon[0])
    list2=list(draw_polygon[1])
import matplotlib.pyplot as plt
plotter = Plotter()
plotter.add_polygon(list1,list2)
plt.show()

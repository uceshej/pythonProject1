from plotter import Plotter
import matplotlib.pyplot as plt
plotter = Plotter()
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
    # plotter.add_point(point_x_all, point_y_all, 'inside')

#         point_x_all.append(float(point_x))
#         point_y_all.append(float(point_y))
#     list3=list(point_x_all)
#     list4=list(point_y_all)
# plt.plot(list3,list4,'ro')

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
    list1=list(polygon_x_all)
    list2=list(polygon_y_all)

# plotter.add_polygon(list1,list2)
# plotter.add_point(point_x_all, point_y_all, )
# plt.show()



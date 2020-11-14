
with open('polygon.csv','r') as f:
    plot=f.readlines()[1:]
    #print(plot)
    #polygon_points = []
    polygon_x_all=[]
    polygon_y_all=[]
    draw_polygon=()
    for row in plot:
        each_rows=row.strip('\n')
        #print(each_rows)
        each_row=each_rows.split(',')
        #print(each_row)
        polygon_id=each_row[0]
        polygon_x=each_row[1]
        polygon_y=each_row[2]
        #print(polygon_x)
        #polygon_list=(polygon_id,polygon_x,polygon_y)
        polygon_x_all.append(int(polygon_x))
        polygon_y_all.append(int(polygon_y))
        #print(polygon_x_all)
        #print(polygon_y_all)
    draw_polygon=(polygon_x_all,polygon_y_all)
    list1=list(draw_polygon[0])
    list2=list(draw_polygon[1])
    #print(list1)
    #print(draw_polygon)
import matplotlib.pyplot as plt
plt.plot(list1,list2)
plt.show()
#plt.plot([0, 0, 1, 3, 4, 4, 3, 3, 2, 1, 1, 2, 3, 2, 2, 4, 4, 3, 1, 0],[1, 6, 7, 7, 6, 4, 4, 5, 6, 5, 2, 1, 2, 2, 3, 3, 1, 0, 0, 1])
plt.show()

        #polygon_show=[]
#plt.plot(polygon_list[2]
#plt.show()

       # print(int(each_row))

#print('each_row',each_row)
#print(plot)
#print(each_row)

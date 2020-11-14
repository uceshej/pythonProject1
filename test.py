with open('polygon.csv','r') as f:
    plot=f.readlines()[1:]

    for row in plot:
        each_rows=row.strip('\n')
        each_row = each_rows.split(',')
        polygon_x = each_row[1]
        polygon_y = each_row[2]
        point_list=[int(polygon_x),int(polygon_y)]

        print(point_list)
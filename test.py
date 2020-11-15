

with open('polygon.csv', 'r') as f:
    plot = f.readlines()[1:]
    line_point=[]
    line_list=[]
    for row in plot:
        each_rows = row.strip('\n')
        each_row = each_rows.split(',')
        line_point=[float(each_row[1]),float(each_row[2])]
        line_list.append(line_point)

with open('polygon.csv','r') as f:
    lo_boundary=[]
    lo_outside=[]

    plot=f.readlines()[1:]
    polygon_x_all=[]
    polygon_y_all=[]

    for row in plot:
        each_rows=row.strip('\n')
        each_row=each_rows.split(',')
        polygon_id=each_row[0]
        polygon_x=each_row[1]
        polygon_y=each_row[2]
        point=(float(polygon_x),float(polygon_y))
        x=point[0]
        y=point[1]

        for i in range(len(line_list)-1):
            line=line_list[i:i+2]
            x1=line[0][0]
            x2=line[0][1]
            y1=line[1][0]
            y2=line[1][1]
            if (x==x1 and y==y1) or (x==x2 and y==y2):
                lo_boundary.append(point)
            elif y1==y1==y:
                if x1<=x<=x2 or x2<=x<=x1:
                    lo_boundary.append(point)
                else:
                    lo_outside.append(point)
            elif x1==x2==x:
                if y1<=y<=y2 or y2<=y<=y1:
                    lo_boundary.append(point)
                else:
                    lo_outside.append(point)











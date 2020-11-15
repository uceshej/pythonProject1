

with open('polygon.csv', 'r') as f:
    plot = f.readlines()[1:]
    line_point=[]
    line_list=[]
    for row in plot:
        each_rows = row.strip('\n')
        each_row = each_rows.split(',')
        line_point=[float(each_row[1]),float(each_row[2])]
        line_list.append(line_point)

with open('input.csv','r') as f:
    lo_boundary=[]
    lo_outside=[]
    lo_inside=[]

    plot=f.readlines()[1:]
    point_x_all=[]
    point_y_all=[]

    for row in plot:
        each_rows=row.strip('\n')
        each_row=each_rows.split(',')
        point_id=each_row[0]
        point_x=each_row[1]
        point_y=each_row[2]
        point=[point_id,float(point_x),float(point_y),'null']
        x=point[1]
        y=point[2]
        #
        count=0
        for i in range(len(line_list)-1):
            line=line_list[i:i+2]
            x1=line[0][0]
            x2=line[0][1]
            y1=line[1][0]
            y2=line[1][1]
            if (x==x1 and y==y1) or (x==x2 and y==y2):
                point[3]=('boundary')
                lo_boundary.append(point)
            elif y1==y2==y:
                if x1<=x<=x2 or x2<=x<=x1:
                    point[3]=('boundary')
                    lo_boundary.append(point)
            elif x1==x2==x:
                if y1<=y<=y2 or y2<=y<=y1:
                    point[3]=('boundary')
                    lo_boundary.append(point)
            elif y1<=y<y2 or y2<=y<y1:
                cross=(y-y1)*(x2-x1)/(y2-y1)+x1
                if cross>x:
                    count+=1
        if count%2!=0 and point[3]!='boundary':
            point[3]=('inside')
            lo_inside.append(point)
        elif count%2==0 and point[3]!='boundary':
            point[3]=('outside')
            lo_outside.append(point)
        print(point)

















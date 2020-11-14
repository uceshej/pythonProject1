import matplotlib.pyplot as plt
x=[]
y=[]
xy_id=[]
with open('polygon.csv','r') as f:
    plot=f.readlines()[1:]
    print(plot)
    for row in plot:
        each_rows=row.strip('\n')
        #print(each_rows)
        each_row=each_rows.split(',')
        #print(each_row)
        polygon_id=each_row[0]
        polygon_x=each_row[1]
        polygon_y=each_row[2]
        polygon_list=[polygon_id,polygon_x,polygon_y]
        print(polygon_list)

       # print(int(each_row))

#print('each_row',each_row)
#print(plot)
#print(each_row)

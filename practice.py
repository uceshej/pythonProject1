import matplotlib.pyplot as plt
x=[]
y=[]
xy_id=[]
with open('polygon.csv','r') as f:
    plot=f.readlines()[1:]
    print(plot)
    for row in plot:
        each_rows=row.strip('\n')
        print(each_rows)


       # print(int(each_row))

#print('each_row',each_row)
#print(plot)
#print(each_row)

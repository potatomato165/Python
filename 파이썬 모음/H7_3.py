A={'May':{9:['Susan','Ceci']}, 'June':{14:['Stephen','Erin'],21:['Bill']}, 'July':{1:['Jay']}}
names={}
for m,value in A.items():
    for d,value2 in value.items():
        for name in value2:
            names[name]=[m,d]
for x,y in names.items():
    print("{}'s birthday : {}/{}".format(x,y[0],y[1]))

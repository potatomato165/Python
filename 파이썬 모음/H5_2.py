data = [1,2,3,4,5,6,7,8,9,10]
S=sum(data)
x=S/len(data)
e=data[1::2]
E=sum(e)
o=data[0::2]
O=sum(o)
data.insert(0,O)
data.insert(1,E)
data.append(x)
print(data)

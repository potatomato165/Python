x=1 ;L=[]
while x<=10:
    a=input('Enter number {} : '.format(x))
    a=int(a)
    L.append(a)
    x+=1
print('The smallest number is {}.'.format(min(L)))

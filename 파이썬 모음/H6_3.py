import random
a=int(input('Enter an integer : '))
bigData=[] ; noData=[]
for x in range(1,101):
    x=int(x)
    b=random.randrange(1, a+1)
    bigData.append(b)
for y in range(1,a+1):
    if y not in bigData:
        noData.append(y)
print(bigData)
print("존재하지 않는 값(들) : {}".format(noData))


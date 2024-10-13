L=list(input("Enter numbers : ").split())
P=[] 
for x in L:
    x=int(x)
    pc=True
    for y in range(2,x):
        if x%y==0:
            pc=False
            break
    if pc==True:
        P.append(x)
print('Prime number : {}'.format(P))

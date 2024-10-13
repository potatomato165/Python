x=open("question.txt",'r')
q=1 ; a=1
while True:
    y=x.readline()
    if not y:
        break
    if y =='+++++\n':
        print('')
        a=1
        print("Q{}. {}?".format(q,x.readline().strip()))
        q+=1
    else:
        print('{}. {}'.format(a,y),end='')
        a+=1
x.close()

import math
print('두 점의 좌표를 입력하시오.')
X1,Y1,Z1=input("X1,Y1,Z1 : ").split()
X2,Y2,Z2=input("X2,Y2,Z2 : ").split()
d=math.sqrt((float(X2)-float(X1))**2+(float(Y2)-float(Y1))**2+(float(Z2)-float(Z1))**2)
print("두 점 ({}, {}, {}) ({}, {}, {})의 거리는 {:.2f}이다".format(X1,Y1,Z1,X2,Y2,Z2,d))

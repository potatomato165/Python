import math
def isValid(s1, s2, s3):
    if s1+s2<=s3 or s1+s3<=s2 or s2+s3<=s1 :
        return False
    else:
        return True
    

'''

   Parameters :

s1, s2, s3(integer) – each side of triangle

   Return value :

True – if sum of two sides is larger than other side

      False - otherwise

'''

   # 이 부분을 완성

 

def area(s1, s2, s3):
    m=(s1+s2+s3)/2
    area=math.sqrt(m*(m-s1)*(m-s2)*(m-s3))
    return area
'''

   Parameters :

s1, s2, s3(integer) – each side of triangle

   Return value :

area of triangle

'''

   # 이 부분을 완성

 

#main
s1, s2, s3=input("세변의 길이 : ").split()
s1=int(s1) ; s2=int(s2) ; s3=int(s3)
if isValid(s1, s2, s3)==True:
    anwser=area(s1, s2, s3)
    print('삼각형의 면적 : %.2f' % anwser)
elif isValid(s1, s2, s3)==False:
    print("입력이 잘못되었습니다.")

# 이 부분을 완성

Dict={}
def countChar(s):
    for x in s:
        if Dict.get(x,0)==0:
            Dict[x]=1
        else:
            Dict[x]=int(Dict[x])+1
    return Dict

inString= input('Enter string : ')
print('='*30)
inString=inString.lower()
Anw=countChar(inString)
for y in Anw.items():
    print("{} : {}번 사용되었습니다.".format(y[0].y[1]))

'''

Parameter : strings

Return Value : dictionary consists of char:count element

'''

# 이 부분을 완성

 

#main

# 이 부분을 완성

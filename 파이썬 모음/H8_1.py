import random
alphabet=['z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p']
special=['!','@','#','$','%','^','&','*','0','1','2','3','4','5','6','7','8','9']
allL=[]
allL.extend(alphabet)
allL.extend(special)
def password(length) :
    L=[]
    L.append((random.choice(alphabet)).upper())
    for x in range(1, length):
        a=random.choice(allL)
        L.append(a)
    pw=''.join(L)
    return pw


'''    parameter : 비밀번호의 길이
    return value : 길이가 length인 비밀번호(문자열)
'''
# 함수를 완성하시오
#main
# 이 부분을 완성
length=int(input("Enter the length of password : "))
pw=password(length)
print("Password is {}".format(pw))

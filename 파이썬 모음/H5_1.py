L=input("단어를 입력하시오 : ")
L=list(L)
ay=['a','y']
V=['a','e','i','o','u']
print(L)
if not L[0] in V:
    X=L[1::]
    X.append(L[0])
    X.extend(ay)
    print(X)
    print("{} ==> {}".format(''.join(L),''.join(X)))
if L[0] in V:
    X=L.copy()
    X.extend(ay)
    print(X)
    print("{} ==> {}".format(''.join(L),''.join(X)))

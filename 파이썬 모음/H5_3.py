L=list(input("8bits 2진수를 입력하십시오 : "))
print(L)
sb=L[0]
print("sign bit : %s" % (sb))
x=L[1:7:]
x.insert(0,sb)
x.insert(1,sb)
print(x)
print("{} ==> {}".format(''.join(L),''.join(x)))


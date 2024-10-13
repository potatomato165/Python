print("Enter two 2-digit numbers")
a=input()
b=input()
if a[0]==b[0] and a[1]==b[1]:
    print("Two numbers({}, {}) are completely same".format(a,b))
elif a[0]==b[1] and a[1]==b[0]:
    print("{} is a reversed number of {}".format(a,b))
elif (a[0]==b[1] and a[1]!=b[0]) or (a[1]==b[0] and a[0]!=b[1]) or (a[1]==b[1] and a[0]!=b[0]) or (a[1]!=b[1] and a[0]==b[0]):
    print("{}, {} : only one digit is same".format(a,b))
elif a[0]!=b[0] and a[1]!=b[1]:
    print("Two numbers({}, {}) are completely different".format(a,b))

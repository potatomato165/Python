a='seojun'
b='IN'
c=2005
d=b.title()+str(c)[-1:-3:-1]+(a.upper())[-1::-1]
print("First Name : %s" % (a))
print("Last Name : %s" % (b))
print("Year of birth : %d" % (c))
print("Login ID : %s" % (d))

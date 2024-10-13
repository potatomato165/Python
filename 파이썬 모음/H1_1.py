w=1000000
usd=w/1146.70
c=w%1146.70
h=usd//100
f=usd%100//50
tw=usd%100%50//20
t=usd%100%50%20//10
o=usd%100%50%20%10
print('달러', '총액 :', str(round(usd)), ',', '거스름돈 :', str(int(c)))
print('100달러 :', str(int(h)))
print('50달러 :', str(int(f)))
print('20달러 :', str(int(tw)))
print('10달러 :', str(int(t)))
print('1달러 :', str(int(o)))

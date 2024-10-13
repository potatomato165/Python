
def isSymmetric(word) :
    result = True
    l = len(word)
    for a in range(l-l//2):
        if word[a] != word[l-a-1]:
            result = False
            break
    return result

x=open('words.txt', 'r')

for b in x:
    if isSymmetric(b.strip())==True:
        print('{} is symmetric'.format(b.strip()))
    if isSymmetric(b.strip())==False:
        print('{} is asymmetric'.format(b.strip()))
x.close()

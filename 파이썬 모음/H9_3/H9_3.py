
def getSubjects(filename):
    x = open(filename, 'r')
    Dict={}
    for a in x:
        a=a.strip()
        a=a.split()
        for b in range(1,len(a)):
            if Dict.get(a[b],0)==False:
                Dict[a[b]] = 1
            else:
                Dict[a[b]] += 1
    x.close()
    return Dict

Dict = getSubjects('timetable.txt')
for s,t in Dict.items():
    print("{} - {}".format(s.title(),t))

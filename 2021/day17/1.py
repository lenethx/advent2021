def isnum(s):
    try:
        int(s)
    except:
        return(False)
    else:
        return int(s)
a=open('input.txt')
coords=list(map(lambda x : list(map(lambda y: list(map(isnum, y.split('..'))),x.split('='))),a.readline()[13:].split(',')))
x1=coords[0][1][0]
x2=coords[0][1][1]
y1=coords[1][1][0]
y2=coords[1][1][1]
finalyvel=min(y1,y2)
#finalyvel=-abs(y1-y2)
maxheight=sum([x for x in range(0, abs(finalyvel))])
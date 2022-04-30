import numpy as np
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
potvels=[]
for x in range(13,max(x1,x2)+1):
    for y in range(min(y1,y2)-1,164):
        #print(x,y)
        point=[0,0]
        vel=[x,y]
        while point[0]<=max(x1,x2) and point[1]>=min(y1,y2) :
            
            if min(x1,x2) <= point[0] <= max(x1,x2) and min(y1,y2) <= point[1] <= max(y1,y2):
                potvels.append([x,y])
                break
            point=[point[0]+vel[0],point[1]+vel[1]]
            vel=[np.sign(vel[0])*(abs(vel[0])-1), vel[1]-1]
            #print(point,x,y)
print(len(potvels))
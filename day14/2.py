a=open("input.txt")
template=a.readline()[:-1]
keypairs=list(map(lambda x: x[:-1].split(' -> '),a.readlines()[1:]))
keys=dict(zip(map(lambda x: x[0],keypairs),map(lambda x: x[1],keypairs)))
newkeys=dict()
initpairs=zip(template, template[1:])
print(template)
amounts=dict()
lettercount=dict()
for item in keys:
    amounts[item]=0
emptyamounts=amounts.copy()
for x in keys:
    newkeys[x]=[x[0]+keys[x],keys[x]+x[1]]
for item in list(keys.values()):
    lettercount[item]=0
    
#define nextpoly(plist):
    
for x in initpairs:
    amounts[''.join(list(x))]+=1

for x in range(0,40):
    amounts2=emptyamounts.copy()
    for y in amounts:
        amounts2[newkeys[y][0]]+=amounts[y]
        amounts2[newkeys[y][1]]+=amounts[y]
    amounts=amounts2

for x in amounts:
    lettercount[x[0]]+=amounts[x]
    lettercount[x[1]]+=amounts[x]
for x in lettercount:
    lettercount[x]/=2
lettercount[template[0]]+=0.5
lettercount[template[-1]]+=0.5
fvals=list(lettercount.values())
fvals.sort()

print(fvals[-1]-fvals[0])
a=open("input.txt")
template=a.readline()[:-1]
keypairs=list(map(lambda x: x[:-1].split(' -> '),a.readlines()[1:]))
keys=dict(zip(map(lambda x: x[0],keypairs),map(lambda x: x[1],keypairs)))
print(template)
amounts=dict()
for item in list(keys.values()):
    amounts[item]=0
    
for x in range(0,10):
    newstr=''
    for x,y in zip(template, template[1:]):
        newstr+=x+keys[x+y]
    template=newstr+template[-1]
    #print(template)

for x in template:
    amounts[x]+=1
fvals=list(amounts.values())
fvals.sort()
print(len(template))
print(fvals[-1]-fvals[0])
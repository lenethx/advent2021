
with open("input.txt") as file:
    data=file.readlines()
sum=0
cnum=""
gearneighbors=set()
digits = [str(x) for x in range(10)]
geardata = [[[] for x in range(len(data[0]))] for y in range(len(data))]
relpos = [
    (-1,-1),
    (-1,0),
    (-1,1),

    (0,-1),
    (0,1),

    (1,-1),
    (1,0),
    (1,1),
]


for num, line in enumerate(data):
    for chnum ,char in enumerate(line):
        if not char in digits:
            if cnum!="":
                for gear in gearneighbors:
                    geardata[gear[0]][gear[1]].append(int(cnum))
                cnum=""
                gearneighbors = set()
                
        elif char in digits:
            cnum+=char
            for y,x in relpos:
                try:
                    if data[num+y][chnum+x] == "*":
                        gearneighbors.add((num+y, chnum+x))
                except:
                    pass

for y, line in enumerate(geardata):
    for x, pset in enumerate(line):
        if len(pset)==2:
            sum+=pset[0]*pset[1]

print(sum)

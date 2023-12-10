with open("input.txt") as file:
    data = [x[:-1] for x in file.readlines()]

dirstring = data[0]
areamapstrings = data[2:]
areamap = {x[:3]: ( x[7:10], x[12:15]) for x in areamapstrings}


locs = [x for x in areamap.keys() if x[-1]=="A"]
steps=0
while any(loc[-1]!="Z" for loc in locs):
    for mapdir in dirstring:
        for index, loc in enumerate(locs):
            locs[index] = areamap[loc][0 if mapdir == "L" else 1]
        steps+=1
        if all(loc[-1]=="Z" for loc in locs):
            break
print(steps)



with open("input.txt") as file:
    data = [x[:-1] for x in file.readlines()]

dirstring = data[0]
areamapstrings = data[2:]
areamap = {x[:3]: ( x[7:10], x[12:15]) for x in areamapstrings}

loc = "AAA"
steps=0
while loc!="ZZZ":
    for mapdir in dirstring:
        loc = areamap[loc][0 if mapdir == "L" else 1]
        steps+=1
        if loc == "ZZZ":
            break
print(steps)



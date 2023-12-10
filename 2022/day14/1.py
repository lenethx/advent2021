import re
with open("input.txt") as file:
    lines=file.read()

xvals=[int(i) for i in re.findall(r"(\d*),", lines)]
yvals=[int(i) for i in re.findall(r",(\d*)", lines)]

sandmat=[[" " for x in range(min(xvals), max(xvals)+1)]  for y in range(0, max(yvals)+1)  ]

for line in lines.split("\n")[:-1]:
    rockcoords = line.split(" -> ")
    for i in range(0, len(rockcoords)-1):
        coord1=[int(j) for j in rockcoords[i].split(",")]
        coord2=[int(j) for j in rockcoords[i+1].split(",")]
        if coord1[0]==coord2[0]:
            for y in range(min(coord1[1], coord2[1]),max(coord1[1], coord2[1])+1):
                sandmat[y][coord1[0]-min(xvals)]="#"
        else:
            for x in range(min(coord1[0], coord2[0]),max(coord1[0], coord2[0])+1):
                sandmat[coord1[1]][x-min(xvals)]="#"

units=0
outofrange=True
try:
    while outofrange:
        grain=(500-min(xvals), 0)
        while True:
            y=grain[1]
            x=grain[0]
            if sandmat[y+1][x]==" ":
                grain=(x,y+1)
            elif sandmat[y+1][x-1]==" ":
                grain=(x-1,y+1)
            elif sandmat[y+1][x+1]==" ":
                grain=(x+1,y+1)
            else:
                sandmat[y][x]="o"
                units+=1
                break

            print(units, grain)
            if not ( grain[0] in range(0,len(sandmat[0])) and grain[1] in range(0, len(sandmat)) ):
                outofrange=False
                break
except:
    pass

print(units)

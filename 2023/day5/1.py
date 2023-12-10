import copy
def parsemap(maptext):
    lines = maptext.split("\n")[1:]
    if lines[-1]=='':
        lines.pop()
    return [[int(y) for y in line.split(" ")] for line in lines]

with open("input.txt") as file:
    data = file.read()# [x[:-1] for x in file.readlines()]
"""

class newrange:
    def __init__(self, smrng):
        if type(smrng)==range:
            self.innerranges = [[smrng[0], smrng[-1]]]
        else:
            self.innerranges = [smrng.copy()]

    def __str__(self):
        return f"{self.innerranges}"

    def union(self, otherrange):
        if type(otherrange) == list:
            outranges = [otherrange]
        elif type(otherrange) == range:
            outranges = [otherrange[0], otherrange[-1]]
        else:
            outranges = copy.deepcopy(otherrange.innerranges)

        for outrange in outranges:
            range
            for inrange in self.innerranges:
                beginrange=None
                endrange=None
                if inrange[0] >= outrange[0] >= inrange[1]:
                    beginrange = outrange[0]
                if inrange[0] >= outrange[1] >= inrange[1]:
                    endrange = outrange[1]

                if beginrange!=None and endrange!=None:
                    break
                elif beginrange!=None and endrange==None:
                    outranges.append(inrange[1], outrange[1])
                elif beginrange==None and endrange!=None:
                    outranges.append(outrange[0], inrange[0])
                else:
                    self.innerranges.append(outrange)

        self.cleanup()


    def cleanup(self):
        pass
            

    def contains(self, x):
        for inrange in self.innerranges:
            if inrange[0] >= x >= inrange[1]:
                return True
        return False

"""



maps = data.split("\n\n")

startseedstring = maps[0].split(":")[1][1:]
startseeds = startseedstring.split(" ")
maplis = [parsemap(x) for x in maps[1:]]

currentranges = [int(x) for x in startseeds]

print(currentranges)
for x_to_y_map in maplis:
    newranges=[]
    for rang in currentranges:
        wasfound=False
        for mapline in x_to_y_map:
            if mapline[1] <= rang <= mapline[1]+mapline[2]:
                wasfound=True
                diff =  mapline[0]-mapline[1]
                print(rang, mapline, rang+diff, "?")
                newranges.append(rang+diff)
                break
        if not wasfound:
            newranges.append(rang)
    currentranges = newranges
print(currentranges)
print(min(currentranges))
"""
for x_to_y_map in maplis:
    
    newranges=[]
    for rang in currentranges:
        wasfound = False

        for mapline in x_to_y_map:
            unionset = set(range(mapline[0], mapline[0]+mapline[2])).intersection( set(range(rang[0], rang[1]+1))  )
            if unionset:
                diff =  mapline[1]-mapline[0]
                newranges.append([min(unionset)+diff, max(unionset)+diff])

    print(newranges,"\n\n")
    currentranges = newranges

"""     






import copy
def parsemap(maptext):
    lines = maptext.split("\n")[1:]
    if lines[-1]=='':
        lines.pop()
    return [[int(y) for y in line.split(" ")] for line in lines]

with open("i.txt") as file:
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


def batched(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

maps = data.split("\n\n")

startseedstring = maps[0].split(":")[1][1:]
startseeds = startseedstring.split(" ")
maplis = [parsemap(x) for x in maps[1:]]

currentranges = [[int(x), int(y)] for x,y in batched(startseeds, 2)]

def morph(morphline, morphrange): # returns [morphedrange, [unmorpheedranges]]
    diff =  morphline[0]-morphline[1]
    unmorphedranges = []
    if morphline[1] < morphrange[0]:
        if morphline[1]+morphline[2]-1 >= morphrange[0]:
            morphedrange =  [morphrange[0]+diff, min(morphrange[1]+diff, morphline[0]+morphline[2]-1)]
            if morphline[1]+morphline[2]-1 < morphrange[1]:
                unmorphedranges.append([ morphline[1]+morphline[2]+1-1, morphrange[1]])
            print("a", (morphedrange, unmorphedranges))
            return (morphedrange, unmorphedranges)

        else:
            print("b")
            return ([], [morphrange])
    elif morphrange[0] >= morphline[1] >=morphrange[1]:
        morphedrange = [morphline[1]+diff, min(morphrange[1]+diff, morphline[0]+morphline[2]-1)]
        unmorphedranges.append([morphrange[0], morphline[1]-1])
        if morphline[1]+morphline[2]-1 < morphrange[1]:
            unmorphedranges.append([ morphline[1]+morphline[2]+1-1, morphrange[1]])
        print("c")
        return (morphedrange, unmorphedranges)
    else:
        print("d")
        return ([], [morphrange])


print(currentranges)
for x_to_y_map in maplis:
    newranges=[]
    for rang in currentranges:
        for mapline in x_to_y_map:
            if not rang: continue
            newrange, unchangedranges = morph(mapline, [rang[0], rang[0]+rang[1]])
            if newrange:
                newrange = [newrange[0], newrange[1]-newrange[0]]
                newranges.append(newrange)
                unchangedranges = [[x[0], x[1]+x[0]] for x in unchangedranges]
                for unchangedrange in unchangedranges:
                    currentranges.append(unchangedrange)
                rang.clear()
            print(newrange, unchangedranges)
        if rang:
            newranges.append(rang)
    currentranges = newranges
    print(newranges)

print(min([x[0] for x in currentranges]))
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






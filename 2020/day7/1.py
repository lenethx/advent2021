with open("input.txt") as file:
    lines=file.readlines();
    
def parsebag(bag):
    bag=bag.strip(" .\n")
    if bag[0].isdigit():
        rval = [int(bag[0]), bag[1:]]
    else:
        rval = [0, bag]
    rval[1] = rval[1][:-4].strip()
    return rval

def containsgoldbag(ibag, foundbags):
    for bagtype in bagtypes[ibag]:
        if not bagtype in foundbags:
            foundbags &= containsgoldbag(bagtype, foundbags & bagtype)






bagtypes=dict()
for line in lines:
    bagtype, containedbags=line.split("contain")
    pbagdict=dict()
    for cbag in containedbags.split(","):
        pbagcount, pbagname = parsebag(cbag)
        pbagdict[pbagname] = pbagcount
    bagtypes[parsebag(bagtype)[1]] = pbagdict

def recsum(indir):
    thisval=0
    less10kval=0
    for key, value in indir.items():
        if type(value)==int:
            thisval+=value
        else:
            tx, ty=recsum(value)
            thisval+=tx
            less10kval+=ty
    if thisval<=100000:
        less10kval+=thisval
    return (thisval, less10kval)


def findbestdir(indir, neededspace, smallestneededspace):
    thisval=0
    for key,value in indir.items():
        if type(value)==int:
            thisval+=value
        else:
            tx,ty=findbestdir(value, neededspace, smallestneededspace)
            thisval+=tx
            if smallestneededspace > ty > neededspace:
                smallestneededspace=ty
                print(smallestneededspace, ty, neededspace)
            
            if smallestneededspace > tx > neededspace:
                smallestneededspace=tx
    return (thisval, smallestneededspace)




    
with open("input.txt") as file:
    lines=file.read().split("\n")[:-1]
    root=dict()
    cdir=root
    cdirpath=""
    for line in lines:
        match line[:3]:
            case "$ c":
                if line[5]=='/':
                    cdir=root
                    cdirpath=""
                elif line[5:7]=="..":
                    cdir=root
                    for ddir in cdirpath.split("/")[:-1]:
                        cdir=cdir[ddir]

                    cdirpath="/".join(cdirpath.split("/")[:-1])
                    cdirpath = "" if cdirpath=="/" else cdirpath
                else:
                    if not line[5:] in cdir.keys():
                        cdir[line[5:]]=dict()
                    cdirpath+=("/" if cdirpath !="" else "")+line[5:]
                    cdir=cdir[line[5:]]

            case "$ l":
                pass
            case "dir":
                cdir[line[4:]]=dict()
            case _:
                cdir[line.split(" ")[1]]=int(line.split(" ")[0])

    print(findbestdir(root,  30_000_000 - 70_000_000 + recsum(root)[0], 99999999999999999999))



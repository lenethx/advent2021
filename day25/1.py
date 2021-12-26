def prmat(tmat):
    if isinstance(tmat, dict):
        for tiem in tmat:
            print(f"{tiem}: {tmat[tiem]}")
    else:
        for tiem in tmat:
            print(tiem)

def stepf(fmat):
    sknext=0
    for sublistindex in range(0,len(fmat)):
        place0=fmat[sublistindex][0]
        for charindex in range(0, len(fmat[sublistindex])):
            if sknext==0:
                if fmat[sublistindex][charindex]=='>':
                    if charindex+1==len(fmat[sublistindex]):
                        if place0=='.':
                            fmat[sublistindex][charindex]='.'
                            fmat[sublistindex][0]='>'
                            sknext=1
                    elif fmat[sublistindex][charindex+1]=='.':
                        fmat[sublistindex][charindex]='.'
                        fmat[sublistindex][charindex+1]='>'
                        sknext=1
            else:
                sknext=0
    
    
    places0=fmat[0][:]
    for charindex in range(0,len(fmat[sublistindex])):
        sknext=0
        for sublistindex in range(0, len(fmat)):
            if sknext==0:
                if fmat[sublistindex][charindex]=='v':
                    if sublistindex+1==len(fmat): 
                        if places0[charindex]=='.':
                            fmat[sublistindex][charindex]='.'
                            fmat[0][charindex]='v'
                            sknext=1
                    elif fmat[sublistindex+1][charindex]=='.':
                        fmat[sublistindex][charindex]='.'
                        fmat[sublistindex+1][charindex]='v'
                        sknext=1
            else:
                sknext=0

def countinmat(nfstr):
    tctr=0
    for x in mat:
        for y in mat:
            if y==nfstr:
                tctr+=1
    return tctr
            
with open("i.txt") as file:
    mat=list(map(lambda x: list(x)[:-1] ,file.readlines()))

#prmat(mat)
oldmat=[]
step=0
prmat(mat)
while oldmat!=mat:
    
    oldmat=list(map(lambda x: x[:],mat))
    stepf(mat)
    prmat(list(map(''.join,mat)))
    step+=1
    print(step)
print(step)
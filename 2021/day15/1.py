import sys
sys.setrecursionlimit(10000)
def prmat(tmat):
    for tiem in tmat:
        print(tiem)
a=open("input.txt")
costmat=list(map(lambda x: list(map(lambda y: [int(y),float('inf')],(x[:-1]))) ,a.readlines()))
costmat[0][0][1]=0
posi=[0,0]

def neighbours(pos):
    neig=[]
    if not (pos[1]==len(costmat[0])-1):
        neig.append([pos[0],pos[1]+1])    
    if not (pos[0]==len(costmat)-1):
        neig.append([pos[0]+1,pos[1]])
    if not pos[1]==0:
        neig.append([pos[0],pos[1]-1])
    if not pos[0]==0 :
        neig.append([pos[0]-1,pos[1]])

#    if not (pos[1]==0 or pos[0]==0):
#        neig.append([pos[0]-1,pos[1]-1])
#    if not (pos[1]==0 or pos[0]==len(costmat)-1):
#        neig.append([pos[0]+1,pos[1]-1])
#    if not (pos[1]==len(costmat[0])-1 or pos[0]==0):
#        neig.append([pos[0]-1,pos[1]+1])
#    if not (pos[1]==len(costmat[0])-1 or pos[0]==len(costmat)-1):
#        neig.append([pos[0]+1,pos[1]+1]) 
    #neig.sort(key=lambda x: costmat[x[0]][x[1]][0])
    return neig
#while not (x==len(costneig.append([[0])-1 and y==len(costmat)-1):
ctr=0
ccc=costmat[-1][-1][-1]
def iterdijk(pos,ccc):
    global ctr
    for ne in neighbours(pos):
        #print(costmat[ne[0]][ne[1]][1],costmat[pos[0]][pos[1]][1]+costmat[ne[0]][ne[1]][0])
        if costmat[ne[0]][ne[1]][1]>costmat[pos[0]][pos[1]][1]+costmat[ne[0]][ne[1]][0]:
            costmat[ne[0]][ne[1]][1]=costmat[pos[0]][pos[1]][1]+costmat[ne[0]][ne[1]][0]
            if ccc!=costmat[-1][-1][-1]:
                print(costmat[-1][-1][-1],ctr)
            ctr+=1
            ccc=iterdijk(ne,costmat[-1][-1][-1])
    return(ccc)
    
            

iterdijk(posi,ccc)
print(costmat[-1][-1][-1])
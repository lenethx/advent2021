import time
start_time = time.time()
import sys
sys.setrecursionlimit(10000000)
def rprint(x):
    print(x)
    return x
def prmat(tmat):
    for tiem in tmat:
        print(tiem)
a=open("i.txt")
notcostmat=list(map(lambda x: list(map(lambda y: [int(y),float('inf')],(x[:-1]))) ,a.readlines()))
costmat=[]
for mult in range(0,5):
    for b in notcostmat:
        costmat.append(list(map(lambda x: [int(x[0]+mult),float('inf')] ,b)))    

costmat=list(map(lambda x: x+list(map(lambda y:[int(y[0]+1),float('inf')] ,x))+list(map(lambda y:[int(y[0]+2),float('inf')] ,x))+list(map(lambda y:[int(y[0]+3),float('inf')] ,x))+list(map(lambda y:[int(y[0]+4),float('inf')] ,x)),costmat))
for row in range(0,len(costmat)):
    for col in range(0,len(costmat[row])):
        if costmat[row][col][0]>9:
            costmat[row][col][0]-=9
costmat[0][0][1]=0
posi=[0,0]

def neighbours(pos):
    neig=[]
    if not pos[1]==0:
        neig.append([pos[0],pos[1]-1])
    if not pos[0]==0 :
        neig.append([pos[0]-1,pos[1]])
    if not (pos[1]==len(costmat[0])-1):
        neig.append([pos[0],pos[1]+1])    
    if not (pos[0]==len(costmat)-1):
        neig.append([pos[0]+1,pos[1]])
#    if not (pos[1]==0 or pos[0]==0):
#        neig.append([pos[0]-1,pos[1]-1])
#    if not (pos[1]==0 or pos[0]==len(costmat)-1):
#        neig.append([pos[0]+1,pos[1]-1])
#    if not (pos[1]==len(costmat[0])-1 or pos[0]==0):
#        neig.append([pos[0]-1,pos[1]+1])
#    if not (pos[1]==len(costmat[0])-1 or pos[0]==len(costmat)-1):
#        neig.append([pos[0]+1,pos[1]+1]) 
    return neig
#while not (x==len(costneig.append([[0])-1 and y==len(costmat)-1):

ctr=0
def iterdijk(pos, ctr):
    for ne in neighbours(pos):
        #print(costmat[ne[0]][ne[1]][1],costmat[pos[0]][pos[1]][1]+costmat[ne[0]][ne[1]][0])
        if costmat[ne[0]][ne[1]][1]>costmat[pos[0]][pos[1]][1]+costmat[ne[0]][ne[1]][0]:
            costmat[ne[0]][ne[1]][1]=costmat[pos[0]][pos[1]][1]+costmat[ne[0]][ne[1]][0]
            ctr+=1
            if ctr>1000000:
                print(costmat[-1][-1][-1])
                ctr=0
            ctr=iterdijk(ne,ctr)
    return ctr
            

iterdijk(posi,0)
print(costmat[-1][-1][-1])
print("--- %s seconds ---" % (time.time() - start_time))

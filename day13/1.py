import numpy as np
def prmat(tmat):
    for tiem in tmat:
        print(tiem)
        

a=open("input.txt")
lines=a.readlines()
dots=list(map(lambda x: list(map(int,x.split(','))),lines[:lines.index('\n')]))
folds=list(map(lambda x: [x[11],int(x[13:-1])],lines[lines.index('\n')+1:]))

y=[]
for item in dots:
    y+=[item[1]]
mlen=max(y)+1
y=[]
for item in dots:
    y+=[item[0]]
mwid=max(y)+1
afm=[0 for x in range(0,mwid)]
mat=[afm.copy() for x in range(0,mlen)]

for item in dots:
    mat[item[1]][item[0]]=1
#prmat(mat)


def foldmat(mmat,line,dir):
    if dir=='x':
        arr1=list(map(lambda i : i[:line],mmat))
        arr2=list(map(lambda i : i[line+1:],mmat))
        while len(arr1[0])>len(arr2[0]):
            arr2=list(map(lambda i: i+[0],arr2))
        while len(arr1[0])<len(arr2[0]):
            arr2=list(map(lambda i: [0]+i,arr2))
        arr2=list(map(lambda i: i[::-1],arr2))
    else:
        arr1=mmat[:line]
        arr2=mmat[line+1:]
        while len(arr1)>len(arr2):
            arr2.append([0 for x in range(0,len(arr1[0]))])
        while len(arr1)<len(arr2):
            arr1.insert(0,[0 for x in range(0,len(arr1[0]))])
        arr2.reverse()
    
    
    return (np.array((arr1))+np.array((arr2))).tolist()


ctr=0
mat=foldmat(mat,folds[0][1],folds[0][0])
#print()
#prmat(mat)
for y in mat:
    for x in y:
        if x>0:
            ctr+=1

print( ctr)
                
            


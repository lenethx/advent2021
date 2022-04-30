from numpy import sign
def recint(mlist):
    thlist=mlist.copy()
    for x in range(0, len(thlist)):
       # print(thlist[x], list,str)
        if isinstance(thlist[x], list):
            thlist[x]=recint(thlist[x])
        elif isinstance(thlist[x], str):
            thlist[x]=int(thlist[x])
    return thlist

a=open('input.txt')
boards=recint(list(map(lambda y: [y[0].split(","),y[1].split(",")], (list(map(lambda x: x.split("->"), list(map(lambda w: w[0:-1], a.readlines()))))))))


    
        


mat=[]
line=[]
for t in range(0,1000):
    line.append(0)
for t in range(0,1000):
    mat.append(line.copy())

i=0
while i < len(boards):
        xval=boards[i][0][0]
        yval=boards[i][0][1]
        dirX=sign(boards[i][1][0]-boards[i][0][0])
        dirY=sign(boards[i][1][1]-boards[i][0][1])
        mat[xval][yval]+=1
        while not (xval==boards[i][1][0] and yval==boards[i][1][1]):
            xval+=dirX
            yval+=dirY
            mat[xval][yval]+=1
        #mat[xval+dirX][yval+dirY]+=1
        i+=1
    
#print(mat)
fc=0
for x in mat:
    for y in x:
        if y>1:
            fc+=1
            
print(fc)

def prmat(tmat):
    for tiem in tmat:
        print(tiem)
#prmat(mat)
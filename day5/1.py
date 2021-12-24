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
    print(i,boards[i])
    if boards[i][0][0]==boards[i][1][0]:
        #print(boards[i][0][1] if boards[i][0][1] < boards[i][1][1] else boards[i][1][1],boards[i][0][1]+1 if boards[i][0][1] > boards[i][1][1] else boards[i][1][1]+1 )
        #print(boards[i])
        for x in range(boards[i][0][1] if boards[i][0][1] < boards[i][1][1] else boards[i][1][1],boards[i][0][1]+1 if boards[i][0][1] > boards[i][1][1] else boards[i][1][1]+1 ):
            
            mat[boards[i][0][0]][x]+=1
            #print(mat[x][boards[i][0][1]])
    elif boards[i][0][1]==boards[i][1][1]:
        #print(boards[i])
        #print(boards[i][0][0] if boards[i][0][0] < boards[i][1][0] else boards[i][1][0],boards[i][0][0]+1 if boards[i][0][0] > boards[i][1][0] else boards[i][1][0]+1)
        for x in range(boards[i][0][0] if boards[i][0][0] < boards[i][1][0] else boards[i][1][0],boards[i][0][0]+1 if boards[i][0][0] > boards[i][1][0] else boards[i][1][0]+1 ):
                mat[x][boards[i][0][1]]+=1
     
    i+=1
    
#print(mat)
fc=0
for x in mat:
    for y in x:
        if y>1:
            fc+=1
            
print(fc)
a=open("input.txt")
mat=list(map(lambda x: list(map(lambda y: int(y),(x[:-1]))) ,a.readlines()))
flashtally=0

def prmat(tmat):
    for tiem in tmat:
        print(tiem)
p=0
while True:
    
    prmat(mat)
    print('')
    #print(p)
    mat=list(map(lambda x: list(map(lambda y: y+1,x)), mat))
    
    nineexists=1
    while nineexists: 
        nineexists=0
        for x in range(0,len(mat)):
            for y in range(0,len(mat[x])):
                if mat[x][y] > 9:
                    mat[x][y] =0
                    nineexists=1
                    flashtally+=1
                   #print(1)
                    if not (x==0 or mat[x-1][y] == 0):
                        mat[x-1][y]+=1
                    if not (y==0 or mat[x][y-1] == 0 ):
                        mat[x][y-1]+=1
                    if not (x==len(mat)-1 or mat[x+1][y] == 0 ):
                        mat[x+1][y]+=1    
                    if not (y==len(mat[x])-1 or mat[x][y+1] == 0 ):
                        mat[x][y+1]+=1
                    if not (x==0 or y==0 or mat[x-1][y-1] == 0):
                        mat[x-1][y-1]+=1
                    if not (x==0 or y==len(mat[x])-1 or mat[x-1][y+1] == 0):
                        mat[x-1][y+1]+=1
                    if not (x==len(mat)-1 or y==0 or mat[x+1][y-1] == 0):
                        mat[x+1][y-1]+=1
                    if not (x==len(mat)-1 or y==len(mat[x])-1 or mat[x+1][y+1] == 0):
                        mat[x+1][y+1]+=1  
    if sum(map(lambda x : sum(x), mat))==0:
        print(p+1)
        break
    p+=1

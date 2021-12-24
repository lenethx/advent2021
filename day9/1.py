a=open("input.txt")
mat=list(map(lambda x: list(map(lambda y: int(y),(x[:-1]))) ,a.readlines()))
total=0
for x in range(0,len(mat)):
    for y in range(0,len(mat[x])):
        if (x==0 or mat[x-1][y] > mat[x][y]) and (y==0 or mat[x][y-1] > mat[x][y]) and (x==len(mat)-1 or mat[x+1][y] > mat[x][y]) and (y==len(mat[x])-1 or mat[x][y+1] > mat[x][y]):
            print(x,y)
            total+=1+mat[x][y]
            
print(total)
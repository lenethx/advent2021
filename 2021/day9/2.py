a=open("input.txt")
mat=list(map(lambda x: list(map(lambda y: int(y),(x[:-1]))) ,a.readlines()))
lowpoints=[]
for x in range(0,len(mat)):
    for y in range(0,len(mat[x])):
        if (x==0 or mat[x-1][y] > mat[x][y]) and (y==0 or mat[x][y-1] > mat[x][y]) and (x==len(mat)-1 or mat[x+1][y] > mat[x][y]) and (y==len(mat[x])-1 or mat[x][y+1] > mat[x][y]):
            
            lowpoints.append([x,y])
            
def lowiter(point, points):
    points.append(point)
    if not (point[0]==0 or mat[point[0]-1][point[1]] == 9 or [point[0]-1,point[1]] in points ):
        lowiter([point[0]-1,point[1]],points)
    if not (point[1]==0 or mat[point[0]][point[1]-1] == 9 or [point[0],point[1]-1] in points ):
        lowiter([point[0],point[1]-1],points)
    if not (point[0]==len(mat)-1 or mat[point[0]+1][point[1]] == 9 or [point[0]+1,point[1]] in points ):
        lowiter([point[0]+1,point[1]],points)    
    if not (point[1]==len(mat[point[0]])-1 or mat[point[0]][point[1]+1] == 9 or [point[0],point[1]+1] in points ):
        lowiter([point[0],point[1]+1],points)
    return points

basins=[]
for v in lowpoints:
    a=[]
    basins.append(lowiter(v,a))
    
basinlen=list(map(lambda x: len(x), basins))
basinlen.sort(reverse=True)
print(basinlen[0]*basinlen[1]*basinlen[2])
    
with open("input.txt") as file:
    fnums=list(map(list, file.read().split("\n")[:-1]))
fclusters = [ [ False for j in i  ] for i in fnums ]
fdistance = [ [ False for j in i  ] for i in fnums ]
clusters=[]

order="SabcdefghijklmnopqrstuvwxyzE"

def findcluster(startx, starty, clusterletter, clusternumber):
    if starty >= len(fnums) or startx>=len(fnums[starty]):
        return

    if fclusters[starty][startx] is False:
        if fnums[starty][startx]==clusterletter:
            fclusters[starty][startx]=clusternumber
            findcluster(startx+1, starty, clusterletter, clusternumber)
            findcluster(startx-1, starty, clusterletter, clusternumber)
            findcluster(startx, starty+1, clusterletter, clusternumber)
            findcluster(startx, starty-1, clusterletter, clusternumber)
    else:
        diff=order.find(clusterletter)-order.find(fnums[starty][startx])
        if abs(diff) == 1:
            clusters[clusternumber][1].add(fclusters[starty][startx])
            clusters[fclusters[starty][startx]][1].add(clusternumber)
        elif diff > 1:
            clusters[clusternumber][1].add(fclusters[starty][startx])
        elif diff < -1:
            clusters[fclusters[starty][startx]][1].add(clusternumber)


for y in range(0, len(fnums)):
    for x in range(0, len(fnums[y])):
        if fclusters[y][x] is False:
            clusters.append([fnums[y][x], set(), False])
            findcluster(x,y, fnums[y][x], len(clusters)-1)
        
        if fnums[y][x]=='S':
            sposition=(x,y)



firstcluster=list(filter(lambda x: True if x[0]=='S' else False, clusters))[0]
firstclusterindex=clusters.index(firstcluster)

def shortestpath(incluster, clusters, path):
    print(path)
    if clusters[incluster][0]=="E":
       
        return path

    clusters=list(map(lambda x: x.copy(), clusters))
    clusters[incluster][2]=True
    paths=[]
    for clusterindex in clusters[incluster][1]:
        if clusters[clusterindex][2]==False:
            path2=shortestpath(clusterindex, clusters, path+(clusterindex,))
            if path2:
                paths.append(path2)
    return sorted(paths, key=len)[-1] if len(paths) else False
                  

path=shortestpath(firstclusterindex, clusters, (firstclusterindex,))



iters=0
distances=[]
def iteralg(x, y, distance):
    global iters
    global distances
    global fdistance
    global fnums
    global fclusters
    if not ( fdistance[y][x] is False or fdistance[y][x]>distance):
        return
    fdistance[y][x]=distance
    iters+=1
    if iters % 100000 ==0:
        print("\n\n")
        for line in fdistance:
            print(line)
        print("\n\n")
    if fnums[y][x]=='E':
        print("E is in", distance)
        distances.append(distance)
        return

    if x<len(fnums[0])-1 and fclusters[y][x+1] in path and path.index(fclusters[y][x+1]) - path.index(fclusters[y][x]) in range(0,2):
        iteralg(x+1, y, distance+1)
    if x>0 and fclusters[y][x-1] in path and path.index(fclusters[y][x-1]) - path.index(fclusters[y][x]) in range(0,2):
        iteralg(x-1, y, distance+1)
    if y<len(fnums)-1 and fclusters[y+1][x] in path and path.index(fclusters[y+1][x]) - path.index(fclusters[y][x]) in range(0,2):
        iteralg(x, y+1, distance+1)
    if y>0 and fclusters[y-1][x] in path and path.index(fclusters[y-1][x]) - path.index(fclusters[y][x]) in range(0,2):
        iteralg(x, y-1, distance+1)


iteralg(sposition[0],sposition[1],0)

print(fdistance[sposition[1]][sposition[0]])

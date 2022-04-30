a=open("input.txt")
connections=list(map(lambda x: x[:-1].split('-'),a.readlines()))
#print(connections)
caves=set()
[caves.add(connections[x][0]) for x in range(0,len(connections))]
[caves.add(connections[x][1]) for x in range(0,len(connections))]

def reccave(cave,prevcaves,twiceused):
    if cave=='end':
        #print(prevcaves)
        return 1
    
    thiscons=[]
    for connection in connections:
        if connection[0]==cave:
            thiscons.append(connection[1])
        elif connection[1]==cave:
            thiscons.append(connection[0])
    total=0
    
    for connection in thiscons:
        #print(connection,connection.isupper(),not connection in prevcaves,"",debugarr)
        if connection.isupper() or not connection in prevcaves:
            total+=reccave(connection,prevcaves+[cave],twiceused)
        elif prevcaves.count(connection)==1 and twiceused==False:
            total+=reccave(connection,prevcaves+[cave],True)
    return total

print(reccave('start',['start'],False))
                
        

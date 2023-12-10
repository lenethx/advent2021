import numpy as np
import math
vec=np.array

with open ("input.txt") as file:
    lines=file.read().split("\n")[:-1]
    
    tail=vec([0,0])
    head=vec([0,0])
    positions={(0,0)}

    dirs={'R':vec([1,0]), 'L': vec([-1,0]), 'U': vec([0,1]), 'D': vec([0,-1])}
    
    for line in lines:
        for i in range(0, int(line[2:])):
            head=head+dirs[line[0]]
            #if math.sqrt((head-tail)[0]**2 + (head-tail)[1]**2)>=2:
            if abs(head[0]-tail[0])==2:
                tail[0]=tail[0]+(head[0]-tail[0])/2
                tail[1]=tail[1]+(head[1]-tail[1])
            
            if abs(head[1]-tail[1])==2:
                tail[1]=tail[1]+(head[1]-tail[1])/2
                tail[0]=tail[0]+(head[0]-tail[0])
            
            positions.add(tuple(tail))
    
    print(len(positions))

        

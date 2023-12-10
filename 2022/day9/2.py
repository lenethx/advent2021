import numpy as np
import math
vec=np.array

def prpos(snek):
    mat=[["." for x in range(-20,20)] for y in range(-20,20)]
    for i, item in enumerate(snek):
        mat[item[1]+20][item[0]+20]=str(i)
        print(str(i), item[1]+20, item[0]+20)
    for line in reversed(mat):
        print(''.join(line))
    print("\n\n")


with open ("input.txt") as file:
    lines=file.read().split("\n")[:-1]
    
    snek=[vec([0,0]) for part in range(0,10)]
    positions={(0,0)}

    dirs={'R':vec([1,0]), 'L': vec([-1,0]), 'U': vec([0,1]), 'D': vec([0,-1])}
    
    # prpos(snek)
    for line in lines:
        for i in range(0, int(line[2:])):
            snek[0]=snek[0]+dirs[line[0]]

            
            for part in range(1,len(snek)):
                head=snek[part-1]
                tail=snek[part]
                if abs(head[0]-tail[0])==2:
                    tail[0]=tail[0]+(head[0]-tail[0])/2
                    tail[1]=tail[1]+np.sign((head[1]-tail[1]))
                
                if abs(head[1]-tail[1])==2:
                    tail[1]=tail[1]+(head[1]-tail[1])/2
                    tail[0]=tail[0]+np.sign((head[0]-tail[0]))
            
            positions.add(tuple(snek[-1]))
        # prpos(snek)
    
    print(len(positions))

        

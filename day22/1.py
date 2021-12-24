def intifint(a):
    try:
        return int(a)
    except:
        return a

def prmat(tmat):
    if isinstance(tmat, dict):
        for tiem in tmat:
            print(f"{tiem}: {tmat[tiem]}")
    else:
        for tiem in tmat:
            print(tiem)

with open("input.txt") as file:
    lines=list(map(lambda x :list(map(lambda y: list(map(lambda z:list(map(lambda w:list(map(intifint,w.split('..'))),z.split('='))),y.split(','))),x[:-1].split(' '))),file.readlines()))
    lines=list(map(lambda x : [x[0][0][0][0], [x[1][0][1][0],x[1][0][1][1]],[x[1][1][1][0],x[1][1][1][1]],[x[1][2][1][0],x[1][2][1][1]] ] ,lines))
    
mat={z:{y:{x:0 for x in range(-50,51)} for y in range(-50,51)} for z in range(-50,51)}
#prmat(lines)
#prmat(mat)
for count,line in enumerate(lines):
    print(count)
    switchto=1 if line[0]=='on' else 0
    for z in mat:
        for y in mat[z]:
            for x in mat[z][y]:
                if ( min(line[3][0],line[3][1]) <= z <= max(line[3][0],line[3][1]) ) and ( min(line[2][0],line[2][1]) <= y <= max(line[2][0],line[2][1]) ) and ( min(line[1][0],line[1][1]) <= x <= max(line[1][0],line[1][1]) ):
                    mat[z][y][x]=switchto
                    #print(f"{x},{y},{z}")
    # for x in range(line[1][0],line[1][1]+1):
        # for y in range(line[2][0],line[2][1]+1):
            # for z in range(line[3][0],line[3][1]+1):
                # if
ctr=0
for z in mat:
    for y in mat[z]:
        for x in mat[z][y]:
            if mat[z][y][x]==1:
                ctr+=1
print(ctr)
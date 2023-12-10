def prmat(mat): 
    for item in mat:
        print(''.join(map(str, item)))

with open("input.txt") as file:
    f=file.read().split("\n")[:-1]
    vism=[[0]*len(f[0]) for item in range(0, len(f))]
    
    for y in range(0, len(f)):
        minheight=int(f[y][0])
        vism[y][0]=1
        for x in range(1, len(f[0])):
            if int(f[y][x]) > minheight:
                vism[y][x]=1
                minheight=int(f[y][x])

        minheight=int(f[y][-1])
        vism[y][-1]=1
        for x in range(len(f[0])-1, 0, -1):
            if int(f[y][x]) > minheight:
                vism[y][x]=1
                minheight=int(f[y][x])


    for x in range(0, len(f[0])):
        minheight=int(f[0][x])
        vism[0][x]=1
        for y in range(1, len(f)):
            if int(f[y][x]) > minheight:
                vism[y][x]=1
                minheight=int(f[y][x])

        minheight=int(f[-1][x])
        vism[-1][x]=1
        for y in range(len(f)-1, 0, -1):
            if int(f[y][x]) > minheight:
                vism[y][x]=1
                minheight=int(f[y][x])

    prmat(vism)
    print(sum(map(sum, vism)))

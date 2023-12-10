def prmat(mat): 
    for item in mat:
        print(''.join(map(str, item)))


def vtl(inlist):
    inlist=list(map(int, inlist))
    tt=0
    ot=inlist[0]
    for item in inlist[1:]:
        if item >= ot:
            tt+=1
            break
        else:
            tt+=1
    return tt



with open("input.txt") as file:
    f=file.read().split("\n")[:-1]
    maxvis=0


    for y in range(0,len(f)):
        for x in range(0, len(f[0])):
            vertlist=list(map(lambda i: i[x], f))
            thisvis= vtl( f[y][x:] ) * \
                     vtl( reversed(f[y][:x+1]) ) * \
                     vtl( vertlist[y:] ) * \
                     vtl( reversed(vertlist[:y+1] ))
            if thisvis > maxvis:
                maxvis=thisvis

    print(maxvis)


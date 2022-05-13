with open("input.txt") as file:
    lines=list(map(lambda x: x[:-1], file.readlines()))


def overflow(num, maxn):

#    print(num)
    while num > maxn:
        num-=maxn
#    print(num)
    return num



extendedlines = list(map(lambda x: x*80, lines))

slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]


def countrees(right, down):
    x=0
    trees=0
    for y,line in enumerate(extendedlines):
        if y % down ==0:
            if line[x]=="#":
                trees+=1
            x+=right
    return trees

tmul=1
for slope in slopes:
    tmul*=countrees(slope[0], slope[1])

print(tmul)


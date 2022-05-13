with open("input.txt") as file:
    lines=list(map(lambda x: x[:-1], file.readlines()))


def overflow(num, maxn):

#    print(num)
    while num > maxn:
        num-=maxn
#    print(num)
    return num



extendedlines = list(map(lambda x: x*39, lines))

x=0
trees=0
for line in extendedlines:
    if line[x]=="#":
        trees+=1
    x+=3

print(trees)

#why is thi not working
"""
x=0
trees=0
for y,line in enumerate(lines):
    if line[overflow(x, len(lines[0])-1)]=="#":
        trees+=1
        extendedlines[y]=extendedlines[y][:x]+"O"+extendedlines[y][:x+1]
    else:
        extendedlines[y]=extendedlines[y][:x]+" "+extendedlines[y][:x+1]
    x+=3
print(trees)

print('\n'.join(list(map(lambda x: x[:200], extendedlines))))

"""

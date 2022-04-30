with open("input.txt") as file:
    lines=list(map(lambda x: x[:-1], file.readlines()))

x=0
trees=0

def overflow(num, maxn):
    while num > maxn:
        num-=maxn
    print(num)
    return num

for line in lines:
    if line[overflow(x, len(lines[0])-1)]=="#":
        trees+=1
    x+=3
print(trees)



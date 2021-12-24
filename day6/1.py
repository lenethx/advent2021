a=open('input.txt')
fishlist=list(map(lambda x: int(x), a.readline().split(',')))

def pday (x):
    if x==0:
        fishlist.append(9)
        return 6
    else:
        return x-1

for x in range(0,80):
    print(x)
    fishlist=list(map(pday, fishlist))
    #print(fishlist)
print(len(fishlist))
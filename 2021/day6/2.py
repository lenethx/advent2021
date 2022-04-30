a=open('input.txt')

def cuontfish(flist):
    rarr=[0,0,0,0,0,0,0,0,0]
    for x in flist: rarr[x]+=1
    return rarr


fishlist=cuontfish(list(map(lambda x: int(x), a.readline().split(','))))
for i in range(0,256):
    fishlist=[fishlist[1],fishlist[2],fishlist[3],fishlist[4],fishlist[5],fishlist[6],fishlist[7]+fishlist[0],fishlist[8],fishlist[0]]

    



print(fishlist)
print(sum(fishlist))

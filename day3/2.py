
a=open("./input.txt")
b=a.readlines()
for x in range(0, len(b)):
    b[x]=b[x][0:-1]

def gret(a,b):
    return a >= b
def lst(a,b):
    return a<b
def findrating (ilist, optbp):
    
    for bit in range(0, len(ilist[0])):
        #print(bit)
        ctr1=0
        for item in ilist:
            if int(item[bit])==1:
                ctr1+=1
#        print(ctr1 , "occurrences of bit 1 out of", len(ilist), "making",ctr1/(len(ilist)/2))
        if optbp(ctr1,len(ilist)/2):
            bitvalue=1
        else:
            bitvalue=0
        print("chosing",bitvalue,"as correct bit value")
        x=len(ilist)-1
        while x>=0:
            if int(ilist[x][bit])!=bitvalue:
                ilist.pop(x)
            x-=1
        #print( ilist)
        if len(ilist)==1:
            
            return ilist[0]
            
c=findrating(b.copy(),gret)
print(b)
d=findrating(b.copy(),lst)

print(c,d,int(c, base=2),int(d, base=2),int(c, base=2)*int(d, base=2))
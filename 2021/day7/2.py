from numpy import sign
a=open('input.txt')
crablist=list(map(lambda x: int(x), a.readline().split(',')))

mflag=True
def recimprove(ilist,curr):
    prevval=sum(list(map(lambda x : sum(range(1,abs(x-(curr-1))+1)),ilist)))
    currentval=sum(list(map(lambda x : sum(range(1,abs(x-curr)+1)),ilist)))
    nextval=sum(list(map(lambda x : sum(range(1,abs(x-(curr+1))+1)),ilist)))
    print(currentval,curr)
    if prevval<currentval:
        return recimprove(ilist,curr-1)
    elif nextval<currentval:
        return recimprove(ilist,curr+1)
    else: 
        return curr 
        
goal=recimprove(crablist,int(sum(crablist)/len(crablist)))

print(sum(list(map(lambda x:sum(range(1,abs(x-goal)+1)) ,crablist))))
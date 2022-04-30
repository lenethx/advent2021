from statistics import median
from numpy import sign
a=open('input.txt')
crablist=list(map(lambda x: int(x), a.readline().split(',')))

mflag=True
def recimprove(ilist,curr):
    prevval=sum(list(map(lambda x : abs(x-(curr-1)),ilist)))
    currentval=sum(list(map(lambda x : abs(x-curr),ilist)))
    nextval=sum(list(map(lambda x : abs(x-(curr+1)),ilist)))
    if prevval<currentval:
        return recimprove(ilist,curr-1)
    elif nextval<currentval:
        return recimprove(ilist,curr+1)
    else: 
        return curr 
        
goal=recimprove(crablist,median(crablist))

print(sum(list(map(lambda x:abs(x-goal) ,crablist))))
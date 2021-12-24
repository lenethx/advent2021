import math
def isnum(s):
    try:
        return int(s)
    except:
        return s

#import ast
a=open("input.txt")
#sfnumbers=list(map(ast.literal_eval,a.readlines()))
sfnumbers=list(map(list,a.readlines()))
sfnumbers=list(map(lambda y:[isnum(x) for x in y if not (x ==',' or x=='\n')],sfnumbers))
def simplifySFN(sfn):
    depth=0
    for x in range(0, len(sfn)):
        if sfn[x]=='[':
            depth+=1
        elif sfn[x]==']':
            depth-=1
        if depth>4:
            bval=sfn[x+1]
            fval=sfn[x+2]
            rl=sfn[:x]+[0]+sfn[x+4:]
            for y in range(x+1,len(rl)):
                if isinstance(rl[y],int):
                    rl[y]+=fval
                    break
                    
            for y in range(x-1,-1,-1):
                if isinstance(rl[y],int):
                    rl[y]+=bval
                    break
            return rl
    for x in range(0, len(sfn)):
        if isinstance(sfn[x],int) and sfn[x]>=10:
            return sfn[:x]+['[',math.floor(sfn[x]/2),math.ceil(sfn[x]/2),']']+sfn[x+1:]
    return sfn
    

def magnitudeofsum(num1, num2):
    olditem=['[']+num1+num2+[']']
    newitem=simplifySFN(olditem)
    while newitem != olditem:
        olditem=newitem
        newitem=simplifySFN(olditem)

    while len(newitem)>3:
        for i in range(0,len(newitem)-2):
            if newitem[i]=='[' and isinstance(newitem[i+1],int) and isinstance(newitem[i+2],int):
                newitem=newitem[:i]+[3*newitem[i+1]+2*newitem[i+2]]+newitem[i+4:]
                break
                
    return newitem[0]
    
magnitudes=[]
for k in sfnumbers:
    for l in sfnumbers:
        magnitudes.append(magnitudeofsum(k,l))
        magnitudes.append(magnitudeofsum(l,k))
print(max(magnitudes))
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
#        print(x, sfn[x])
        if sfn[x]=='[':
            depth+=1
#            print('depth is',depth)
        elif sfn[x]==']':
            depth-=1
#            print('depth is',depth)
        if depth>4:
#            print('depth >4, exploding')
            bval=sfn[x+1]
            fval=sfn[x+2]
            rl=sfn[:x]+[0]+sfn[x+4:]
            for y in range(x+1,len(rl)):
                if isinstance(rl[y],int):
 #                   print('added value',fval,'to position',y,'(',rl[y],')')
                    rl[y]+=fval
                    break
                    
            for y in range(x-1,-1,-1):
                if isinstance(rl[y],int):
#                    print('added value',bval,'to position',y,'(',rl[y],')')
                    rl[y]+=bval
                    break
            return rl
    for x in range(0, len(sfn)):
#        print(x,sfn[x])
        if isinstance(sfn[x],int) and sfn[x]>=10:
#            print('greater than 10 found, splitting')
#            print(sfn[:x],']')
#            print(['[',math.ceil(sfn[x]/2),math.floor(sfn[x]/2)])
#            print(sfn[x+1:])
            return sfn[:x]+['[',math.floor(sfn[x]/2),math.ceil(sfn[x]/2),']']+sfn[x+1:]
    return sfn
    
#testsfn=['[', '[', '[', '[', 4, '[', 1, 2, ']', ']', 6, ']', '[', 13, 4, ']', ']', '[', '[', 6, 8, ']', 0, ']', ']']
#print ('',testsfn,'\n',simplifySFN(testsfn),'\n',simplifySFN(simplifySFN(testsfn)))
#"""
newitem=sfnumbers[0]
for item in sfnumbers[1:]:
#    print(newitem)
#    print(item)
    olditem=['[']+newitem+item+[']']
#    print(olditem)
    newitem=simplifySFN(olditem)
    while newitem != olditem:
        #print(newitem)
        olditem=newitem
        newitem=simplifySFN(olditem)
print(newitem,'\n\n')
#"""        
        
"""test        
olditem=[isnum(x) for x in list('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]') if not (x ==',' or x=='\n')]
print(olditem)
newitem=simplifySFN(olditem)
while newitem != olditem:
    
    olditem=newitem
    print(olditem)
    newitem=simplifySFN(olditem)
print(newitem)
"""
while len(newitem)>3:
    for i in range(0,len(newitem)-2):
        if newitem[i]=='[' and isinstance(newitem[i+1],int) and isinstance(newitem[i+2],int):
            newitem=newitem[:i]+[3*newitem[i+1]+2*newitem[i+2]]+newitem[i+4:]
            break
    print(newitem)
            
print(newitem)
from itertools import zip_longest 

#True if list1 is smaller than list2
def complist(list1, list2):
    for item1, item2 in zip_longest(list1, list2):
        if type(item1)==int and type(item2)==int:
            if item2 > item1:
                return True
            elif item2 < item1:
                return False
        elif item1==None:
            return True
        elif item2==None:
            return False
        else:
            result =  complist(item1 if type(item1)==list else [item1], item2 if type(item2)==list else [item2])
            if type(result)==bool:
                return result



with open("input.txt") as file:
    lines=file.read().split("\n")[:-1]

lists=[ eval(x) for x in lines if x!=""]
lists.append([[2]])
lists.append([[6]])

x=True
while x:
    x=False
    for i in range(0, len(lists)-1):
        if not complist(lists[i], lists[i+1]):
            tmp=lists[i]
            lists[i]=lists[i+1]
            lists[i+1]=tmp
            x=True
[print(ll) for ll in lists]
ctr=1
for i, tlist in enumerate(lists):
    if len(tlist)==1 and type(tlist[0])==list and len(tlist[0])==1 and tlist[0][0] in [2,6]:
        ctr*=i+1
#        print(i+1)
print(ctr)


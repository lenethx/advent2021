from itertools import zip_longest 

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


lists=[ [eval(lines[0+x]),eval(lines[1+x])] for x in range(0, len(lines), 3)]

ctr=0
for i, elists in enumerate(lists):
    if complist(*elists):
        ctr+=i+1
print(ctr)

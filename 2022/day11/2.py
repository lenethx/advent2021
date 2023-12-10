import math 

with open("input.txt") as file:
    lines=file.read().split("\n\n")

lines=list(map(lambda x: x.split("\n"), lines))

class monke:
    items = []
    test = lambda x: x
    op = lambda x: x
    inspections = 0

    def __init__(self, items, op, test):
        self.items = items
        self.test = test
        self.op = op

    def inspectandthrow(self):
        if len(self.items)==0:
            return False
        
        self.inspections += 1

        item = self.items.pop(0)
        item = self.op(item)

        return (item,  self.test(item))

    def additem(self, item):
        self.items.append(item)
    

ops={"+":sum, "*": math.prod}

monkeys=list(map( lambda x:  monke(
    list(map(int, x[1][18:].split(","))),
    lambda y: ops[x[2][23]]([y, y if x[2][25:] == "old" else int(x[2][25:])]),
    lambda y: int(  x[4][29:] if y % int(x[3][21:])==0 else x[5][30:]  )

                            )  , lines ))

subbal=math.prod(map( lambda x: int(x[3][21:]) , lines))
print(subbal)
for round in range(0, 10000):
    for monkey in monkeys:
        while ret:=monkey.inspectandthrow():
            #while ret[0] > subbal:
            #    ret=(ret[0]-subbal, ret[1])

            if ret[0]!=0:
                ret=(ret[0] % subbal, ret[1])
        
            monkeys[ret[1]].additem(ret[0])
    print(round)

#for monkey in monkeys:
#    print(monkey.inspections)
print(ops["*"]( sorted(map( lambda x: x.inspections, monkeys ) )[-2:] ))


class list2(list):
     def map(self, lambdafunction):
         return list2(map(lambdafunction, self))

l2=list2

with open("input.txt") as file:
    data=file.read().split("\n\n")
    piledata=data[0].split("\n")[:-1]
    piles=[[] for i in range(0,9)]
    for x in range(len(piledata)-1,-1, -1):
        lines=[piledata[x][y+1:y+2] for y in range(0, len(piledata[x]), 4)]
        for count, item in enumerate(lines):
            if item != ' ':
                piles[count].append(item)
    

    movedata=data[1].split("\n")[:-1]
    for item in movedata:
        parts=item.split(" ")
        for count in range(0, int(parts[1])):
            piles[int(parts[5])-1].append(piles[int(parts[3])-1].pop())

    print((l2(piles).map(lambda x: x[-1])))


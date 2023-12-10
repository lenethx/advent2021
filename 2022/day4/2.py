class list2(list):
     def map(self, lambdafunction):
         return list2(map(lambdafunction, self))

l2=list2

with open("input.txt") as file:
    f=l2(file.read().split("\n")[:-1])
    f=f.map(lambda x: l2(x.split(",")).map(lambda x: l2(x.split("-")).map(lambda x: int(x))  ))
 

    res=f.map(lambda x: min(x[0][1]-x[0][0]+1, x[1][1]-x[1][0]+1) if (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or  (x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) else max(0, min(x[0][1]-x[1][0]+1,  x[1][1]-x[0][0]+1))).map(lambda x: bool(x))
    print(sum(l2(res)))

    for item,i2 in zip(f,res):
        print(item,i2)


    

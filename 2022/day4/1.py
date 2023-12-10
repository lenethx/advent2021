class list2(list):
     def map(self, lambdafunction):
         return list2(map(lambdafunction, self))

l2=list2

with open("input.txt") as file:
    f=l2(file.read().split("\n")[:-1])
    f=f.map(lambda x: l2(x.split(",")).map(lambda x: l2(x.split("-")).map(lambda x: int(x))  ))
 

    res=filter(lambda x: (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or  (x[0][0] >= x[1][0] and x[0][1] <= x[1][1]), f)
    print(len(l2(res)))


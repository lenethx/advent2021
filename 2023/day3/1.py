
with open("input.txt") as file:
    data=file.readlines()
sum=0
cnum=""
isadjacent=False
digits = [str(x) for x in range(10)]
relpos = [
    (-1,-1),
    (-1,0),
    (-1,1),

    (0,-1),
    (0,1),

    (1,-1),
    (1,0),
    (1,1),
]


for num, line in enumerate(data):
    for chnum ,char in enumerate(line):
        if not char in digits:
            if cnum!="":
                if isadjacent:
                    sum+=int(cnum)
                cnum=""
                isadjacent=False
                
        elif char in digits:
            cnum+=char
            for y,x in relpos:
                try:
                    if not data[num+y][chnum+x] in digits+[".", "\n"]:
                        isadjacent=True
                except:
                    pass


print(sum)

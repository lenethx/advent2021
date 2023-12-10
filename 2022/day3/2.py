import math
def p(x):
    print(x)
    return x

def tl(x):
    try:
        return tl(list(x))
    except:
        return x

def ptl(x):
    return p(tl(x))

with open("input.txt") as file:
    vals = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines=file.read().split("\n")
    lines=list(map( lambda x: list(set(map(lambda y: 2**vals.find(y), x))) , lines))
    lines=list(map(lambda x: lines[x:x+3]  , range(0, len(lines), 3)))

#    lines=map(lambda x:[list(set(list(x)[:len(x)//2])), list(set(list(x)[len(x)//2:]))], lines)
    
    lines=map(lambda x: math.log2(sum(x[0]) & sum(x[1]) & sum(x[2]))   ,list(lines)[:-1])


    print(sum(lines))

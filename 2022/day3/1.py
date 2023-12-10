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
    lines=map( lambda x: list(map(lambda y: 2**vals.find(y), x)) , lines)
    lines=map(lambda x:[list(set(list(x)[:len(x)//2])), list(set(list(x)[len(x)//2:]))], lines)
    
    lines=map(lambda x: math.log2(sum(x[0]) & sum(x[1]))   ,list(lines)[:-1])


    """
    print( sum( 
        map(lambda x: math.log2(list(x)[0] & list(x)[1]), 
            ptl(map(lambda x: 
                map(lambda x: 
                    map( lambda x: vals.find(x) ,x) ,
                    x) 
                ,lines)  
            )) 
            ) 
          )"""
    print(sum(lines))

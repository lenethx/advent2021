with open("input.txt") as file:
    lines=list(map(lambda x: x[:-1], file.readlines()))

def findplace(inputstring, upperChar, lowerChar):
    totalplaces=2**(len(inputstring)-1)
    place=0
    for ite, char in enumerate(inputstring):
        if char == lowerChar:
           pass
        else:
            place+=totalplaces/(2**ite)
        # print(place, char)
    return place
        
def getseatid(seatcode):
    return (findplace(seatcode[:7],"B","F")*8) + findplace(seatcode[7:], "R", "L")

def getallseats(sofar):
    if len(sofar)==10:
        return [sofar]
    elif len(sofar) >=7:
        return getallseats(sofar+"R")+ getallseats(sofar+"L")
    else:
        return getallseats(sofar+"F")+ getallseats(sofar+"B")

print(set(map(getseatid, getallseats(""))) - set(map(getseatid, lines)) )


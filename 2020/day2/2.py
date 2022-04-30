with open("input.txt") as file:
    lines = file.readlines()
# lines = list(map(lambda x: x[:-1], lines)) # lambdas are cool but its all probably a bad idea for data parsing. Res gular expressions would probably be better

def parsestring(inputstring):
    if inputstring[:-1]:
        print(inputstring)
        a,b,c=inputstring[:-1].split(" ")
        index1,index2= a.split("-")
        return (c[int(index1)-1] == b[:-1]) ^ (c[int(index2)-1] == b[:-1])
    else:
        return False

print(sum(map(parsestring, lines)))

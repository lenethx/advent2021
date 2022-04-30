with open("input.txt") as file:
    lines = file.readlines()
# lines = list(map(lambda x: x[:-1], lines)) # lambdas are cool but its all probably a bad idea for data parsing. Res gular expressions would probably be better

def parsestring(inputstring):
    if inputstring[:-1]:
        a,b,c=inputstring[:-1].split(" ")
        minchars,maxchars= a.split("-")
        return int(minchars) <= c.count(b[:-1]) <= int(maxchars)
    else:
        return False

print(sum(map(parsestring, lines)))

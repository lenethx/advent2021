
with open("input.txt") as file:
    data=file.readlines()

total=0
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits += [str(x) for x in range(10)]
for line in data:
    mindigit=None
    maxdigit=None
    mindigitpos=9999
    maxdigitpos=0
    for digit in digits:
        if -1 < ( z:=line.find(digit) ) < mindigitpos:
            mindigitpos = z
            mindigit = digit if len(digit)<2 else digits.index(digit)
        while ( z:=line.find(digit, maxdigitpos+1) )> -1:
            maxdigitpos = z
            maxdigit = digit if len(digit)<2 else digits.index(digit)
    print(line, mindigit, maxdigit, num, total)
    maxdigit = mindigit if maxdigit == None else maxdigit
    num = int(str(mindigit) + str(maxdigit))
    total += num
print(total)

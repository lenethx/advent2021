
with open("input.txt") as file:
    data=file.readlines()

total=0
digits = [str(x) for x in range(10)]
for line in data:
    mindigit=9999
    maxdigit=0
    for digit in digits:
        if -1 < ( z:=line.find(digit) ) < mindigit:
            mindigit = z 
        while ( z:=line.find(digit, maxdigit+1) )> -1:
            maxdigit = z

    num = int(str(line[mindigit]) + str(line[maxdigit]))
    total += num
print(total)

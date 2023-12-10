with open("input.txt") as file:
    lines=file.read().split("\n")[:-1]

cycle=0
register=1
sumint=0
for line in lines:
    for x in range(0, 1 if line[:4]=="noop" else 2):
        cycle+=1
        if (cycle-20) % 40 ==0 and cycle < 222:
            sumint+=cycle*register
    if line[:4]=="addx":
        register+=int(line[5:])

print(sumint)
print(register)

    

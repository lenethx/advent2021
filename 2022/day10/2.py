with open("input.txt") as file:
    lines=file.read().split("\n")[:-1]

cycle=0
register=1
ops=[]



for line in lines:
    if line[:4]=="addx":
        ops.append("noop")
    ops.append(line)

oplines=[ops[i:i + 40] for i in range(0, len(ops), 40   )]
for opline in oplines:
    line=""
    for i, op in enumerate(opline):
        line+="#" if i in range(register-1, register+2) else " "
        if op[:4]=="addx":
            register+=int(op[5:])
    print(line)



    

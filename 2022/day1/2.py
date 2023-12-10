with open("input.txt") as file:
    highest=[]
    highest2=[0,0,0]
    current=0
    for line in map(lambda x: x[:-1], file.readlines()):
        if line == "":
            for x in range(0, 3):
                if current>highest2[x]:
                    highest2[x]=current
                    highest2.sort()
                    break
            
            highest.append(current)
            current=0
            
        else:
            current+=int(line)
    highest.sort()
    print(highest)
    print(highest2)
    print(sum(highest[-3:]))
    print(sum(highest2))

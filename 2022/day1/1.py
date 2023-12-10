with open("input.txt") as file:
    highest=0
    current=0
    for line in map(lambda x: x[:-1], file.readlines()):
        if line == "":
            if current>highest:
                highest=current
            current=0
        else:
            current+=int(line)

    print (highest)

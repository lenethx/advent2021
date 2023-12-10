with open("input.txt") as file:
    ctr=0
    f=file.read()
    while len(set(f[0+ctr:14+ctr]))!=14:
        ctr+=1
    print(ctr+14)
    

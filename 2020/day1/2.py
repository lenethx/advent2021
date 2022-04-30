with open("input.txt") as file:
    lines=file.readlines();
    lines = list(map(lambda x: int(x[:-1]), lines))

    
    
for ci, i in enumerate(lines):
    for cj, j in enumerate(lines):
        if cj > ci:
            for ck, k in enumerate(lines):
                if ck > cj and i + j + k == 2020:
                    print (i,j,k,i*j*k)

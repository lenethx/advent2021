with open("input.txt") as file:
    data = [x[:-1] for x in file.readlines()]

times = [x for x in data[0].split(":")[1].split(" ") if x != ""]
distances = [x for x in data[1].split(":")[1].split(" ") if x != ""]
times = int("".join(times))
distances = int("".join(distances))

distsoverrecord=0
for ms in range(times+1):
    if ms % 100000 == 0:
        print(ms)
    if (times-ms)*ms > distances:
        distsoverrecord+=1

print(distsoverrecord)

with open("input.txt") as file:
    data = [x[:-1] for x in file.readlines()]

times = [int(x) for x in data[0].split(":")[1].split(" ") if x != ""]
distances = [int(x) for x in data[1].split(":")[1].split(" ") if x != ""]

prodnumways=1

for x in range(len(times)):
    distsoverrecord=0
    for ms in range(times[x]+1):
        if (times[x]-ms)*ms > distances[x]:
            distsoverrecord+=1
    prodnumways*=distsoverrecord

print(prodnumways)

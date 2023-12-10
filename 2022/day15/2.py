import re

def manhattan(coord1, coord2):
    return abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])

with open("input.txt") as file:
    lines=file.read()



coordlist=re.findall(r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)", lines)

for y in range(0, 4000001):
    ranges=[]
    for coords in [[int(j) for j in i] for i in coordlist]:
        distance=manhattan((coords[0],coords[1]),(coords[2],coords[3]) )
        xdist=distance-abs(coords[1]-y)
        for rang in ranges:
            if rang[0] > coords[0]-xdist > rang[1]:
                if rang[0] > coords[0]+xdist+1 > rang[1]:
                    pass
                else:

            elif rang[0] > coords[0]+xdist+1 > rang[1]:
                pass
            else: 
                ranges.append(coords[0]-xdist, coords[0]+xdist+1)

ranges=set()
beacons=set()
    print(xdist)
    if xdist>=0:
        ranges.update(set(( range(coords[0]-xdist, coords[0]+xdist+1  ) )))
    if coords[3]==2000000:
        beacons.add(coords[3])

ranges.difference_update(beacons)
print(len(ranges))

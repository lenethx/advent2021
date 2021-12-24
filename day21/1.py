with open("input.txt") as file:
    p1pos=int(file.readline()[-2])
    p2pos=int(file.readline()[-2])
print(p1pos,p2pos)
class deterministicdie:
    def __init__(self):
        self.value=0
        self.rolls=0
    def roll(self):
        self.value=1 if self.value>=100 else self.value+1
        self.rolls+=1
        return self.value
        
a=deterministicdie()

p1score=0
p2score=0
while p1score<1000 and p2score<1000:
    #print(p1pos,p1score,p2pos,p2score)
    p1pos+=a.roll()+a.roll()+a.roll()
    #print(p1pos)
    while p1pos>10:
        p1pos-=10
    #print(p1pos)
    p1score+=p1pos
    if p1score>=1000:
        break
    p2pos+=a.roll()+a.roll()+a.roll()
    while p2pos>10:
        p2pos-=10
    p2score+=p2pos
    
print(min(p1score,p2score)*a.rolls)
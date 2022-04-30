with open("input.txt") as file:
    op1pos=int(file.readline()[-2])
    op2pos=int(file.readline()[-2])
print(op1pos,op2pos)
"""
class deterministicdie:
    def __init__(self):
        self.value=0
        self.rolls=0
    def roll(self):
        self.value=1 if self.value>=100 else self.value+1
        self.rolls+=1
        return self.value
        
a=deterministicdie()


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
"""

ppos=dict()
for p1score in range(0,22):
    for p2score in range(0,22):
        for p1pos in range(1,11):
            for p2pos in range(1,11):
                ppos[(p1score,p2score,p1pos,p2pos,0)]=0
                ppos[(p1score,p2score,p1pos,p2pos,1)]=0

p1wins=0
p2wins=0
dicevals={3:1,4:3,5:6,6:7,7:6,8:3,9:1}
ppos[(0,0,op1pos,op2pos,0)]=1
fornow=[(0,0,8,9,0)]
for iteration in range(0,22):
    print(iteration)
    # for key in ppos:
        # if ppos[key]>0:
            # print(key,ppos[key])
    for key in ppos:  
        # if key in fornow:
            # print(f"key previously modified! {key} has {ppos[key]} timelines")
            
        if key[-1]==0:
            factor=ppos[key]
            for possiblevalue in dicevals:
                p1pos=key[2]+possiblevalue
                if p1pos>10:
                    p1pos-=10
                p1score=p1pos+key[0]
                if p1score>=21:
                    p1wins+=dicevals[possiblevalue]*factor
                    # if key in fornow:
                        # print(f"added {dicevals[possiblevalue]*factor} wins")
                else:
                    ppos[(p1score,key[1],p1pos,key[3],1)]+=dicevals[possiblevalue]*factor
                    # if key in fornow:
                        # print(f"added {dicevals[possiblevalue]*factor} timelines to {(p1score,key[1],p1pos,key[3],1)}")
                        # fornow.append((p1score,key[1],p1pos,key[3],1))
        else:
            factor=ppos[key]
            for possiblevalue in dicevals:
                p2pos=key[3]+possiblevalue
                if p2pos>10:
                    p2pos-=10
                p2score=p2pos+key[1]
                if p2score>=21:
                    p2wins+=dicevals[possiblevalue]*factor
                    # if key in fornow:
                        # print(f"added {dicevals[possiblevalue]*factor} wins")
                else:
                    ppos[(key[0],p2score,key[2],p2pos,0)]+=dicevals[possiblevalue]*factor
                    # if key in fornow:
                        # print(f"added {dicevals[possiblevalue]*factor} timelines to {(key[0],p2score,key[2],p2pos,0)}")
                        # fornow.append((key[0],p2score,key[2],p2pos,0))                
            
        ppos[key]=0
        
for key in ppos:
    if ppos[key]>0:
        print(key,ppos[key])
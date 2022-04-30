def intifint(a):
    try:
        return int(a)
    except:
        return a






            

with open("input.txt") as file: 
    instructions=list(map(lambda x: list(map(intifint,x[:-1].split(' ')))+ ([0] if x[0]=='i' else []) ,file.readlines()))
    
    
z=1
input=100000000000000
cycles=0
while z!=0:
    if cycles>10000:
        cycles=0
        print(inputs)
    input=input-1
    cycles+=1
    inputs=str(input)
    if '0' in str(inputs):
        input-=1
        continue
    w=0
    x=0
    y=0
    z=0
    ctr=0


    for item in instructions:
        item1=globals()[item[1]]
        item2=globals()[item[2]] if isinstance(item[2],str) else item[2]
        #print(item2)
        if item[0]=='inp':
            globals()[item[1]]=int(inputs[ctr])
            ctr+=1
        elif item[0]=='add':
            globals()[item[1]]=item1+item2
        elif item[0]=='mul':
            globals()[item[1]]=item1*item2
        elif item[0]=='div':
            globals()[item[1]]=int(item1/item2)
        elif item[0]=='mod':
            globals()[item[1]]=item1%item2
        elif item[0]=='eql':
            globals()[item[1]]= 1 if item1==item2 else 0
     
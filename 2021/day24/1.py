def intifint(a):
    try:
        return int(a)
    except:
        return a

def testnumber(number):
    w=0
    x=0
    y=0
    z=0
    ctr=0
    inputs=str(number)
    if '0' in inputs:
        return False
    for item in instructions:
        item1=locals()[item[1]]
        item2=locals()[item[2]] if isinstance(item[2],str) else item[2]
        #print(item2)
        if item[0]=='inp':
            print(item1,item2)
            exec(f"{item[1]}=int(inputs[ctr])")
            #locals()[item[1]]=int(inputs[ctr])
            ctr+=1
        elif item[0]=='add':
            locals()[item[1]]=item1+item2
        elif item[0]=='mul':
            locals()[item[1]]=item1*item2
        elif item[0]=='div':
            locals()[item[1]]=int(item1/item2)
        elif item[0]=='mod':
            locals()[item[1]]=item1%item2
        elif item[0]=='eql':
            locals()[item[1]]= 1 if item1==item2 else 0
        print(w,x,y,z)
    print(locals())
    if z==0:
        return True
    else:
        return False


            
with open("input.txt") as file: 
    instructions=list(map(lambda x: list(map(intifint,x[:-1].split(' ')))+ ([0] if x[0]=='i' else []) ,file.readlines()))
    
testnumber(12345678912345)
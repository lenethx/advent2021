a=open("input.txt")
inputs=list(map(lambda w: list(map(lambda x: list(map(set,x.split(" "))),w[0:-1].split(" | "))), a.readlines()))
#print(inputs)
#boards=recint(list(map(lambda y: [y[0].split(","),y[1].split(",")], (list(map(lambda x: x.split("->"), list(map(lambda w: w[0:-1], a.readlines()))))))))
totals=[0,0,0,0,0,0,0,0,0,0]
for item in inputs:
    numbers=[False,False,False,False,False,False,False,False,False,False]
    for digits in item[0]:
        if len(digits)==2:
            numbers[1]=digits
        if len(digits)==3:
            numbers[7]=digits
        if len(digits)==7:
            numbers[8]=digits    
        if len(digits)==4:
            numbers[4]=digits   
    l562=[[],[]]
    templist=list(numbers[1])
    for digits in item[0]:
        if not templist[0] in digits:
            l562[0].append(digits)
        elif not templist[1] in digits:   
            l562[1].append(digits)
        elif len(digits)==5:
            numbers[3]=digits
        elif digits==numbers[1] or digits==numbers[7] or digits==numbers[8] or digits==numbers[4]:
            pass
        elif set.union(digits,numbers[4])==numbers[8]:
            numbers[0]=digits
        else:
            numbers[9]=digits
    if len(l562[0])>len(l562[1]):
        numbers[2]=l562[1][0]
        l562=l562[0]
    else:
        numbers[2]=l562[0][0]
        l562=l562[1]
    if len(l562[0])>len(l562[1]):
        numbers[6]=l562[0]
        numbers[5]=l562[1]
    else:
        numbers[6]=l562[1]
        numbers[5]=l562[0]
    for digits in item[1]:
        totals[numbers.index(digits)]+=1
        
print(totals[1]+totals[4]+totals[7]+totals[8])
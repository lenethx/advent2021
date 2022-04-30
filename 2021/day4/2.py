def dtcalc ():
    
    a=open('input.txt')
    numbers=list(map(lambda x:int(x),a.readline().split(",")))
    boards= list(map(lambda x: x.split(" "), a.readlines()[1:]))
    rboards=[]
    for x in range(0,len(boards), 6):
        for y in range(0,5):
            while '' in boards[x+y]:
                boards[x+y].remove('')
            boards[x+y][-1]=boards[x+y][-1][0:-1]
        rboards.append(boards[x:x+5]) 

    def isequal (array):
        if array[0]== array[1] and array[0]== array[2] and array[0]== array[3] and array[0]== array[4]:
            return True
        else:
            return False
                    
    for num in numbers:
        for w in range(0,len(rboards)):
            
            for x in range(0,len(rboards[w])):
                for y in range(0,len(rboards[w][x])):
                    if str(num)==rboards[w][x][y]:
                        rboards[w][x][y]=''
            for x in range(0,len(rboards[w])):
                if isequal(rboards[w][x]) or isequal([rboards[w][0][x],rboards[w][1][x],rboards[w][2][x],rboards[w][3][x],rboards[w][4][x]]):
                    ssfar=0
                    for u in rboards[w]:
                        for i in u:
                            if i:
                                print(i)
                                ssfar+=int(i)
                    print(ssfar*num)
        f=0
        while f < len(rboards)-1:
            if isequal (rboards[f][0]) or isequal (rboards[f][1]) or isequal (rboards[f][2]) or isequal (rboards[f][3]) or isequal (rboards[f][4])  or isequal([rboards[f][0][0],rboards[f][1][0],rboards[f][2][0],rboards[f][3][0],rboards[f][4][0]]) or isequal([rboards[f][0][1],rboards[f][1][1],rboards[f][2][1],rboards[f][3][1],rboards[f][4][1]]) or isequal([rboards[f][0][2],rboards[f][1][2],rboards[f][2][2],rboards[f][3][2],rboards[f][4][2]]) or isequal([rboards[f][0][3],rboards[f][1][3],rboards[f][2][3],rboards[f][3][3],rboards[f][4][3]])  or isequal([rboards[f][0][4],rboards[f][1][4],rboards[f][2][4],rboards[f][3][4],rboards[f][4][4]]) :
                rboards.pop(f)
            else:
                f+=1
                
                
    print(rboards[0])
    
print(dtcalc())
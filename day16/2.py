import math
a=open("input.txt")
pureinput=a.readline()
zerocount=0
while pureinput[0]=='0':
    pureinput=pureinput[1:]
    zerocount+=1
pkgstr=bin(int(pureinput,base=16))[2:]
#print(pkgstr)
pkgstr='0000'*zerocount+('0'*(4-(len(pkgstr)%4))+pkgstr if len(pkgstr)%4>0 else pkgstr)

#print(pkgstr)
compstr='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]{};:\'",<.>/?'

def parsepacket(pkgstr):
#    print(pkgstr)
#    print(pkgstr[:3])
    data={
        'str':pkgstr, 'ver':int(pkgstr[:3],base=2),
        'type':int(pkgstr[3:6],base=2)
    }
    pointer=6
    if data['type']==4:
        val=''
        while pkgstr[pointer]=='1':
            val+=pkgstr[pointer+1:pointer+5]
            pointer+=5
        val+=pkgstr[pointer+1:pointer+5]
        data['litval']=int(val,base=2)
        data['subpkgs']=int(val,base=2)
        pointer+=5
 #       print('litval')
    else:
        subpkgsarr=[]
        if pkgstr[pointer]=='1':
            data['lm']=1
            pointer+=1
            subpkgslen=int(pkgstr[pointer:pointer+11],base=2)
            data['spa']=subpkgslen
            pointer+=11
            subpkgsstr=pkgstr[pointer:]
#            print('1',subpkgslen,'{')
            for x in range(0,subpkgslen):
#                print(subpkgsstr)
                temparr=parsepacket(subpkgsstr)
#                print(temparr)
                subpkgsarr.append(temparr[0])
                
                pointer+=len(temparr[0]['str'])-len(temparr[1])
                subpkgsstr=temparr[1]
            
                
                
        else:
            data['lm']=0
            pointer+=1
            subpkgslen=int(pkgstr[pointer:pointer+15],base=2)
            data['spl']=subpkgslen
            pointer+=15
            subpkgsstr=pkgstr[pointer:pointer+subpkgslen]
 #           print('0,',subpkgslen,'{')
            while len(subpkgsstr)>6:
                temparr=parsepacket(subpkgsstr)
                subpkgsarr.append(temparr[0])
                subpkgsstr=temparr[1]
            pointer+=subpkgslen
            
        data['subpkgs']=subpkgsarr
#        print('}')
    return [data,pkgstr[pointer:]]
    
n=parsepacket(pkgstr)

def recsearchver(pkt):
    pkt.pop('str')
    if pkt['type']==4:
        return pkt['ver']
    else:
        return pkt['ver']+ sum([recsearchver(item) for item in pkt['subpkgs']])
            
print(recsearchver(n[0]))

opsarr=[sum, math.prod,min,max, lambda x: x , lambda x: 1 if x[0] > x[1] else 0, lambda x: 1 if x[0] < x[1] else 0,lambda x: 1 if x[0] == x[1] else 0 ]
def evalops(pkt):
    print(pkt)
    if isinstance( pkt['subpkgs'], int):
        return pkt['subpkgs']
    else:
        return opsarr[pkt['type']](list(map(evalops,pkt['subpkgs'])))
    


def prmat(tmat):
    for tiem in tmat:
        print(tiem)

import numpy as np
a=open("input.txt")
algorithm=list(a.readline())
a.readline()
mat=list(map(lambda x: list(x)[:-1] ,a.readlines()))
mat=list(map(lambda x: ['.']*55+x+['.']*55,mat))
mat=[['.']*len(mat[0])]*55+mat+[['.']*len(mat[0])]*55
#print(np.matrix((mat)))
prmat(mat)
print()
currentsymbol='.'
for z in range(0,50):
#    print(z)
    newmat=list(map(lambda p : p[:],mat[:]))

    for y in range(0,len(mat)):
        for x in range(0,len(mat[0])):
            neig=''
            for r in range(-1,2):
                for t in range(-1,2):
                    try:
                        neig+=mat[y+r][x+t]
                    except:
                        neig+=currentsymbol
#            print(neig)
#            print('\n,\n')
#            prcopy=list(map(lambda p : p[:],mat[:]))
#            prcopy[y][x]='O'
#            prmat(prcopy)
#            print(y,x)
#            print('\n,\n')
#            prmat(mat)
            
            newmat[y][x]=algorithm[int(''.join(list(map(lambda d: '0' if d=='.' else '1' ,neig))),base=2)]
#            print('\n')           
#            prmat(mat)
#            print('\n\n')

    currentsymbol='#' if currentsymbol == '.' and algorithm[0]=='#' else '.'
    mat=newmat
    #print('\n,\n')
    #prmat(mat)
    #print('\n,\n')
    print(z)
  
litcount=0  
for x in range(len(mat[x])):
    for y in range(len(mat)):
        if mat[y][x]=='#':
            mat[y][x]=1
            litcount+=1
        else:
            mat[y][x]=0
print(litcount)
#prmat(mat)

mat = np.matrix((mat))
with open('outfile.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.2f')
a=open("input.txt")
lines=a.readlines()
scores=[]
pair={')':'(','}':'{',']':'[','>':'<'}
pair2={'(':1,'[':2,'{':3,'<':4}
val={')':3,'}':1197,']':57,'>':25137}
for line in lines:
    score=0
    linearr=[]
    for x in line:
        if x=='\n':
            for mchar in linearr[::-1]:
                score=score*5+pair2[mchar]
            scores.append(score)
            break
        elif x=='(' or x=='[' or x=='{' or x=='<':
            linearr.append(x)
        elif pair[x] == linearr[-1]:
            linearr.pop(-1)
        else:
            break
scores.sort()
print(scores[int((len(scores))/2)])
#def reclint(str):
#    for x in str:
#        if str[x]=='\n':
#            return False
#        if not (str[x]=='<' or str[x]=='(' or str[x]=='{' or str[x]=='[')
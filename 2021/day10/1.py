a=open("input.txt")
lines=a.readlines()
score=0
pair={')':'(','}':'{',']':'[','>':'<'}
val={')':3,'}':1197,']':57,'>':25137}
for line in lines:
    linearr=[]
    for x in line:
        if x=='\n':
            break
        elif x=='(' or x=='[' or x=='{' or x=='<':
            linearr.append(x)
        elif pair[x] == linearr[-1]:
            linearr.pop(-1)
        else:
            score+=val[x]
            break
print(score)
#def reclint(str):
#    for x in str:
#        if str[x]=='\n':
#            return False
#        if not (str[x]=='<' or str[x]=='(' or str[x]=='{' or str[x]=='[')
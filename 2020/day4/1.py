with open("../debug.py") as file:
        exec(file.read())
with open("input.txt") as file:
    #lines=file.readlines()
    validuwu=0
    fields=set()
    reqfields={"byr", "iyr", "eyr","hgt","hcl","ecl","pid"}
    while a:=file.readline():
        if a =="\n":
            if fields.intersection(reqfields) == reqfields:
                validuwu+=1    
                print(bcolors.OKGREEN,fields, 1)
            else:
                print(bcolors.WARNING,fields)
            fields=set()
        else:
            linefields=list(map(lambda x: x.split(":")[0], a[:-1].split(" ")))
            for lf in linefields:
                fields.add(lf)
print(validuwu)

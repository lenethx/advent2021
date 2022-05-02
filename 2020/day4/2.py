import re
with open("../debug.py") as file:
        exec(file.read())
with open("input.txt") as file:
    #lines=file.readlines()
    validuwu=0
    fields={}
    reqfields={"byr", "iyr", "eyr","hgt","hcl","ecl","pid"}
    fieldconditions={
            "byr": lambda x: 1920 <= int(x) <= 2002,
            "iyr": lambda x: 2010 <= int(x) <= 2020,
            "eyr": lambda x: 2020 <= int(x) <= 2030,
            "hgt": lambda x: ( 150 <= int(x[:-2]) <= 193 ) if x[-2:] == "cm" else ( 59 <= int(x[:-2]) <= 76 ) if x[-2:] == "in" else False,
            "hcl": lambda x: bool(re.match("#[a-f0-9]{6,6}",x)) and len(x)==7,
            "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid": lambda x: x.isdigit() and len(x)==9,
            "cid": lambda x: True
            }

    while a:=file.readline():
        if a =="\n":
            if all( x in fields for x in reqfields ):
                anyinvalid=0
                for field in fields:
                    if not fieldconditions[field](fields[field]):
                        anyinvalid+=1
                if not anyinvalid:
                    validuwu+=1
                
                print(bcolors.OKGREEN,fields, 1)
            else:
                print(bcolors.WARNING,fields)
            fields={}
        else:
            linefields=list(map(lambda x: x.split(":"), a[:-1].split(" ")))
            for lf in linefields:
                fields[lf[0]]=lf[1]
print(validuwu)


"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

"""

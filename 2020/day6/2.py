
with open("input.txt") as file:
    answers=set("qwertyuiopasdfghjklzxcvbnm")
    counter = 0
    while a:=file.readline():
        if a =="\n":
            counter+=len(answers)
            print(answers)
            answers=set("qwertyuiopasdfghjklzxcvbnm")
        else:
            answers &= set(a[:-1])
            print(a)

    print(counter)

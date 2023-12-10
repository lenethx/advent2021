import functools

def gettype(hand):
    cards=dict()
    for letter in hand:
        if letter in cards:
            cards[letter]+=1
        else:
            cards[letter]=1

    cardcounts = list(cards.values())
    cardcounts.sort(reverse=True)
    match cardcounts:
        case [5]:
            return 7
        case [4, 1]:
            return 6
        case [3,2]:
            return 5
        case [3,1,1]:
            return 4
        case [2,2,1]:
            return 3
        case [2,1,1,1]:
            return 2
        case [1,1,1,1,1]:
            return 1

def handval(hand):
    hand=hand[0]
    cardvalues = "23456789TJQKA"
    handtype = gettype(hand)
    handvalue = handtype * 16**5

    for factor, card in zip( [16**4, 16**3, 16**2, 16**1, 16**0],  [i for i in hand]):
        handvalue += cardvalues.find(card)*factor
    return handvalue


with open("input.txt") as file:
    data = [x[:-1] for x in file.readlines()]

hands2bids = [ [(z:=x.split(" "))[0],z[1]]  for x in data]

hands2bids.sort(key=handval)
total=0
for i, hand in enumerate(hands2bids):
    total+=(i+1)*int(hand[1])
print(total)

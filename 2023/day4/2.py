


def parse_line_matches(line):
    cardnumberstr, ournumberstr = line.split("|")
    cardnumberstr = cardnumberstr.split(":")[1]
    cardnumbers = [int(x) for x in cardnumberstr.split(" ") if x != ""]
    ournumbers = [int(x) for x in ournumberstr.split(" ") if x != ""]

    matches = [x in  cardnumbers for x in ournumbers]

    return sum(matches)

def main():
    with open("input.txt") as file:
        data = [x[:-1] for x in file.readlines()]

    linecounts={}
    for linenum, line in enumerate(data):
        linenum+=1
        if linenum in linecounts:
            linecounts[linenum]+=1
        else: 
            linecounts[linenum]=1

        newcards = [x+linenum+1 for x in range(parse_line_matches(line))]
        for card in newcards:
            if card in linecounts:
                linecounts[card]+=linecounts[linenum]
            else:
                linecounts[card]=linecounts[linenum]

            

    print(sum(linecounts.values()))


if __name__ == '__main__':
    main()

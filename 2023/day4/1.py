


def parse_line_points(line):
    cardnumberstr, ournumberstr = line.split("|")
    cardnumberstr = cardnumberstr.split(":")[1]
    cardnumbers = [int(x) for x in cardnumberstr.split(" ") if x != ""]
    ournumbers = [int(x) for x in ournumberstr.split(" ") if x != ""]

    matches = [x in  cardnumbers for x in ournumbers]

    return 2**(sum(matches)-1) if any(matches) else 0

def main():
    with open("input.txt") as file:
        data = [x[:-1] for x in file.readlines()]

    pointsum=0
    for line in data:
        pointsum+=parse_line_points(line)
    print(pointsum)


if __name__ == '__main__':
    main()

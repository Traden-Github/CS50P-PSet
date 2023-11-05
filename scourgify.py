import sys
import csv

if len(sys.argv) == 1 or len(sys.argv) == 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        afterList = []
        with open(sys.argv[1]) as toRead:
            reader = csv.DictReader(toRead)
            for row in reader:
                after = {"name":row["name"], "house":row["house"]}
                afterList.append(after)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        endList = []
        for list in afterList:
            last, first = list["name"].split(", ")
            house = list["house"]
            end = {"first":first, "last": last, "house": house}
            endList.append(end)
        with open(sys.argv[2], "w") as toWrite:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(toWrite, fieldnames=fieldnames)
            writer.writeheader()
            for list in endList:
                writer.writerow({"first":list["first"], "last":list["last"], "house":list["house"]})






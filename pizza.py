import sys
import tabulate
import csv

menu = []

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments ")
    elif len(sys.argv) != 2:
        sys.exit("Too many command-line arguments ")
    else:
        if sys.argv[1].endswith(".csv") == False:
            sys.exit("Wrong file type")
        else:
            try:
                with open(sys.argv[1]) as file:
                    for row in file:
                        x, y, z = row.strip().split(",")
                        header = [x, y, z]
                        break
                    menu.append(csv.reader(file))
                    for line in menu:
                        print(tabulate.tabulate(line, header, tablefmt="grid"))

            except FileNotFoundError:
                sys.exit("File not found")


if __name__ == "__main__":
    main()



import sys

if len(sys.argv) != 2:
    if len(sys.argv) == 1:
        sys.exit("Too few arguments")
    else:
        sys.exit("Too many arguments")
else:
    if sys.argv[1].endswith(".py") == False:
        sys.exit("Invalid file type")
    else:
        fileName = sys.argv[1].strip()
        try:
            with open(fileName) as file:
                count = 0
                for row in file:
                    if row.lstrip().startswith("#"):
                        pass
                    elif len(row.strip()) == 0:
                        pass
                    else:
                        count += 1
        except FileNotFoundError:
            sys.exit("File Not Found")
        else:
            print(count)



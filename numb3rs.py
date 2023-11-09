import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if iPv4 := re.search(r"^([0-9]+\.)([0-9]+\.)([0-9]+\.)([0-9]+)$", ip.strip()):
        for i in [1, 2, 3, 4]:
            number = iPv4.group(i)
            if iPv4.group(i).endswith("."):
                number = number.replace(".","")
            if (0 <= int(number) <= 255) == False:
                return False
        return True
    else:
        return False







if __name__ == "__main__":
    main()

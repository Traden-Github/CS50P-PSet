import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"[^a-zA-Z]um[^a-zA-Z]", s.strip(), re.IGNORECASE)
    count = len(um)
    if re.match(r"um[^a-zA-Z]", s.strip(), re.IGNORECASE):
        count += 1
    if re.search(r"[^a-zA-Z]um$", s.strip(), re.IGNORECASE):
        count += 1
    if re.search(r"^um$", s.strip(), re.IGNORECASE):
        count += 1
    return count





if __name__ == "__main__":
    main()

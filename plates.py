def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    any_useless(s)
    if any_useless(s) == True:
        return False
    if (2 <= len(s) <= 6) == False:
        return False
    if s[0:2].isalpha() == False:
        return False
    number_in_mid(s)
    if number_in_mid == True:
        return False
    zero_prefix(s)
    if zero_prefix(s) == True:
        return False
    return True

def any_useless(in_plate):
    for words in in_plate:
        match words:
            case "," | " " | ".":
                return True


def number_in_mid(maybe):
    for chars in maybe:
        if chars.isnumeric() and maybe[len(maybe)-1].isalpha():
            return True

def zero_prefix(inside):
    number_count = 0
    for words in inside:
        if words.isnumeric():
            number_count += 1
    if inside[0:len(inside)-number_count+1].endswith("0"):
        return True

main()

text = input("Enter some text: ")

for letters in text:
    match letters.lower():
        case "a" | "e" | "i" | "o" | "u":
            print("", sep="", end="")
        case _:
            print(letters, sep="", end="")
print()


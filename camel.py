text = input("Enter a variable name here: ")

for letter in text:
    if letter.islower():
        print(letter, end="")
    else:
        print("_",letter.lower(), sep="", end="")
print()

expression = input("Enter an arithmetic expression: ")

x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if y == "/" and z == "0":
    print("Error!")
elif y == "/":
    print(f"{(x/z):.1f}")
elif y == "*":
    print(f"{(x*z):.1f}")
elif y == "-":
    print(f"{(x-z):.1f}")
elif y == "+":
    print(f"{(x+z):.1f}")

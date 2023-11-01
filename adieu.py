names = []
index = 0

while True:
    try:
        name = input("Name: ")
        names.append(name)
        index += 1
    except EOFError:
        break

print("Adieu, adieu, to ", end="")

if index == 1:
    print(names[index-1])

elif index == 2:
    print(f"{names[index-2]} and {names[index-1]}")

else:
    for i in range(len(names)-1):
        print(f"{names[i]}, ", end="")
    print(f"and {names[index-1]}")




add = 0
total = 0
while total < 50:
    add = int(input("Insert coin here: "))
    if add == 25 or add == 10 or add == 5:
        total += add
        if total < 50:
            print("Amount Due:", 50-total)
    else:
        print("Amount Due:", 50-total)

print("Change Owed:", total-50)

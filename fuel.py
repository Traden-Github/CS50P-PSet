while True:
    expression = input("Enter fraction here: ")

    if "/" in expression:
        x, y = expression.split("/")
        try:
            fraction = int(x) / int(y)
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        else:
            if fraction > 1:
                pass
            elif fraction >= 0.99:
                print("F")
                break
            elif fraction <= 0.01:
                print("E")
                break
            else:
                print(f"{fraction*100:.0f}", "%", sep="")
                break


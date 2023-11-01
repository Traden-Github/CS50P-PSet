import random


def main():
    true_level = get_level()
    correct = 0
    for _ in range(10):
        rng1 = generate_integer(true_level)
        rng2 = generate_integer(true_level)
        answer = rng1 + rng2
        error_count = 0
        while error_count < 3:
            get_answer = input(f"{rng1} + {rng2} = ")
            try:
                get_answer = int(get_answer)
                if get_answer == answer:
                    correct += 1
                    break
                else:
                    print("EEE")
                    error_count += 1
            except ValueError:
                print("EEE")
                error_count += 1
        if error_count == 3:
            print(f"{rng1} + {rng2} = {answer}")
    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            lv = int(input("Level: "))
            if lv == 1 or lv == 2 or lv == 3:
                return lv
            else:
                continue
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    if level == 2:
        return random.randint(10,99)
    if level == 3:
        return random.randint(100,999)
    else:
        null = int("ValueError trigger")


if __name__ == "__main__":
    main()

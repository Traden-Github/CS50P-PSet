import random
while True:
    try:
        level = input("Level: ")
        level = int(level)
        if level <= 0:
            continue
        else:
            break

    except ValueError:
        pass

answer = random.randint(1, level)

while True:
    try:
        guess = input("Take a guess: ")
        guess = int(guess)
        if guess < 1:
            continue
        if guess == answer:
            print("Just right!")
            break
        elif guess < answer:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        pass

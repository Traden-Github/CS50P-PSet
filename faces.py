def convert(into):

    into = into.replace(":)", "🙂").replace(":(", "🙁")

    return into

def main():

    text = input("Enter input here: ")

    text = convert(text)

    print(text)

main()

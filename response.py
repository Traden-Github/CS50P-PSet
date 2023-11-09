import validators

def main():
    email = input("Email: ")
    print(validate(email))

def validate(s):
    if validators.email(s) == True:
        return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    main()

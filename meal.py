def main():
    theTime = input("Enter time: ").strip().lower()
    theTime = convert(theTime)

    if 7 <= theTime <= 8:
        print("breakfast time")
    if 12 <= theTime <= 13:
        print("lunch time")
    if 18 <= theTime <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    if minute.endswith("a.m."):
        minute = minute.rstrip(" a.m.")
    if minute.endswith("p.m."):
        minute = minute.rstrip(" p.m.")
        hour = hour + 12
    minute = int(minute) / 60
    return float(hour + minute)

if __name__ == "__main__":
    main()

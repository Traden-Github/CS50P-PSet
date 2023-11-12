import datetime
import sys
import re
import inflect
p = inflect.engine()


def main():

    if find := re.search(r"(^\d\d\d\d-\d\d-\d\d$)", input("Date of Birth: "), re.IGNORECASE):
        yr, mn, dt = find.group(1).split("-")
        try:
            birth = datetime.date(int(yr), int(mn), int(dt))
            today = datetime.date.today()
            minutes = minutesConverter(today-birth)
            words = p.number_to_words(minutes)
            words = words.replace("and ", "")
            print(f"{words.capitalize()} minutes")

        except ValueError:
            sys.exit("Invalid date")

    else:
        sys.exit("Invalid date")

def minutesConverter(time):
    minutes = f"{(time.total_seconds() / 60):.0f}"
    return int(minutes)





if __name__ == "__main__":
    main()

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^(\d+(?::\d\d)?) ([AP])M to (\d+(?::\d\d)?) ([AP])M$", s):
        if re.search(r":", time.group(1)) != None:
            start_hour, start_minute = time.group(1).split(":")
            start_hour = int(start_hour)
            if start_hour > 12:
                raise ValueError
            elif start_hour == 12 and time.group(2) == "A" and start_minute == "00":
                start_hour = f"00"
            elif start_hour < 10 and time.group(2) == "A":
                start_hour = f"0{start_hour}"
            if int(start_minute) >= 60:
                raise ValueError
            if start_hour == 12 and time.group(2) == "P" and start_minute == "00":
                start_hour = f"12"
            elif time.group(2) == "P":
                start_hour += 12
            start = f"{start_hour}:{start_minute}"
        else:
            start_hour = time.group(1)
            start_hour = int(start_hour)
            if start_hour > 12:
                raise ValueError
            elif start_hour == 12 and time.group(2) == "A":
                start_hour = f"00"
            elif start_hour < 10 and time.group(2) == "A":
                start_hour = f"0{start_hour}"
            if start_hour == 12 and time.group(2) == "P":
                start_hour = f"12"
            elif time.group(2) == "P":
                start_hour += 12
            start = f"{start_hour}:00"
        if re.search(r":", time.group(3)) != None:
            end_hour, end_minute = time.group(3).split(":")
            end_hour = int(end_hour)
            if end_hour > 12:
                raise ValueError
            elif end_hour == 12 and time.group(4) == "A" and end_minute == "00":
                end_hour = f"00"
            elif end_hour < 10 and time.group(4) == "A":
                end_hour = f"0{end_hour}"
            if int(end_minute) >= 60:
                raise ValueError
            if end_hour == 12 and time.group(4) == "P" and end_minute == "00":
                end_hour = f"12"
            elif time.group(4) == "P":
                end_hour += 12
            end = f"{end_hour}:{end_minute}"
        else:
            end_hour = time.group(3)
            end_hour = int(end_hour)
            if end_hour > 12:
                raise ValueError
            elif end_hour == 12 and time.group(4) == "A":
                end_hour = f"00"
            elif end_hour < 10 and time.group(4) == "A":
                end_hour = f"0{end_hour}"
            if end_hour == 12 and time.group(4) == "P":
                end_hour = f"12"
            elif time.group(4) == "P":
                end_hour += 12
            end = f"{end_hour}:00"
        return f"{start} to {end}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Enter a date: ").strip()

    if "," in date:
        mn_dt,yr = date.split(", ")
        mn, dt = mn_dt.split(" ")
        try:
            if int(dt) >= 31:
                continue
            if mn in months:
                if months.index(mn) <= 8:
                    print(yr,"-0", months.index(mn)+1,sep="", end="")
                else:
                    print(yr,"-", months.index(mn)+1, sep="", end="")
                if int(dt) <= 9:
                    print("-0", dt, sep="")
                else:
                    print("-", dt, sep="")
                break
        except ValueError:
            continue
    elif "/" in date:
        mn, dt, yr = date.split("/")
        try:
            if int(dt) > 31 or int(mn) > 12:
                continue
            if int(mn) <= 9:
                print(yr,"-0", mn, sep="", end="")
            else:
                print(yr,"-", mn, sep="", end="")
            if int(dt) <= 9:
                print("-0", dt, sep="")
            else:
                print("-", dt, sep="")
            break
        except ValueError:
            continue
    else:
        continue




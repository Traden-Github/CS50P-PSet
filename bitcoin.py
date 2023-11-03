import json
import requests
import sys


try:
    if len(sys.argv)==2:
        amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv)!=2:
        sys.exit("Too many arguments")
try:
    list = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    lists = list.json()
    dollars =  lists["bpi"]
    stats = dollars["USD"]
    rate = float(stats["rate_float"])
    total = rate * amount
except requests.RequestException:
    sys.exit("Error")
else:
    print(f"${total:,.4f}")









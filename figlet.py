import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

fontList = figlet.getFonts()

if (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    for fonts in fontList:
        check = 0
        if sys.argv[2] == fonts:
            figlet.setFont(font=fonts)
            check = 1
            break
    if check == 0:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    figlet.setFont(random.shuffle(fontList))
else:
    sys.exit("Invalid usage")

text = input("Input: ")

print(figlet.renderText(text))






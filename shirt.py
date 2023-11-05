import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
else:
    name1, extension1 = sys.argv[1].strip().split(".")
    extension1 = extension1.lower()
    name2, extension2 = sys.argv[2].strip().split(".")
    extension2 = extension2.lower()
    while True:
        if extension1 == extension2:
            match extension1:
                case "jpg" | "jpeg" | "png":
                    break
                case _:
                    sys.exit("Wrong file type")
        else:
            match extension1:
                case "jpg" | "jpeg" | "png":
                    match extension2:
                        case "jpg" | "jpeg" | "png":
                            sys.exit("Input and output have different extensions")
                        case _:
                            sys.exit("Invaid output")
                case _:
                    match extension2:
                        case "jpg" | "jpeg" | "png":
                            sys.exit("Invalid input")
                        case _:
                            sys.exit("Input and output both have invalid extensions")
    try:
        shirt = Image.open("shirt.png")
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        size = shirt.size
        muppet = ImageOps.fit(muppet, size)
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])



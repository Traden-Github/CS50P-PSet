import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.match(r"<iframe..*src=(\"https?://(www\.)?youtube.com/embed/[\w\S]+\").*></iframe>", s.strip(), re.DOTALL):
        link = link.group(1).replace("\"", "").replace("youtube.com/embed", "youtu.be")
        if re.search(r"https", link) == None:
            link = link.replace("http", "https")
        if re.search(r"www.", link) != None:
            link = link.replace("www.","")
        return link
    else:
        return None





if __name__ == "__main__":
    main()

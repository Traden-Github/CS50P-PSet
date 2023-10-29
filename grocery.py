def print_list(the_list):
    for items, amount in the_list.items():
        print(amount, items)

def main():
    item_list = {}
    while True:
        try:
            item = input()
        except EOFError:
            print()
            break
        else:
            item = item.upper().strip()
            if item in item_list:
                item_list[item] += 1
            else:
                item_list[item] = 1
            sorted_item_list = dict(sorted(item_list.items()))
    try :
        print_list(sorted_item_list)
    except UnboundLocalError:
        print("",end="")
main()

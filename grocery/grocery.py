def get_grocery_list():
    grocery_list = {}
    try:
        while True:
            item = input()
            item = item.strip().lower()
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass
    return grocery_list

def print_grocery_list(grocery_list):
    sorted_items = sorted(grocery_list.keys())
    for item in sorted_items:
        count = grocery_list[item]
        print(f"{count} {item.upper()}")


grocery_list = get_grocery_list()
print_grocery_list(grocery_list)

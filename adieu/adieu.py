def get_names():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass
    return names


def format_names(names):
    count = len(names)
    if count == 1:
        return names[0]
    elif count == 2:
        return f"{names[0]} and {names[1]}"
    else:
        formatted_names = ", ".join(names[:-1]) + f", and {names[-1]}"
        return formatted_names


def main():
    names = get_names()
    for i in range(len(names)):
        farewell = format_names(names[:i + 1])
        print(f"Adieu, adieu, to {farewell}")


if __name__ == "__main__":
    main()

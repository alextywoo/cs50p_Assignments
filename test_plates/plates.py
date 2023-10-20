def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum() or (len(s) < 2 or len(s) > 6):
        return False
    elif s.isalpha() or s[:2].isalpha() and s[-2:].isnumeric() and s[-2:][0] != "0":
        return True
    else:
        return False

if __name__ == "__main__":
    main()
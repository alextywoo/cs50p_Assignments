import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r'\b(um|Um)\b', s):
        count = sum(1 for _ in matches)
        return count
    else:
        return 0



if __name__ == "__main__":
    main()
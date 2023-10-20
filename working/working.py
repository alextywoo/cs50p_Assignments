import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d{1,2}):?(\d{0,2}) (AM|PM) to (\d{1,2}):?(\d{0,2}) (AM|PM)"
    matches = re.search(pattern, s)
    if matches:
        hour1, minute1, ampm1, hour2, minute2, ampm2 = map(matches.group, (1, 2, 3, 4, 5, 6))
        hour1 = int(hour1)
        hour2 = int(hour2)
        minute1 = int(minute1) if minute1 else 0
        minute2 = int(minute2) if minute2 else 0

        if not (0 <= minute1 <= 59) or not (0 <= minute2 <= 59):
            raise ValueError

        if ampm1 == 'PM' and hour1 != 12:
            hour1 += 12
        elif ampm1 == 'AM' and hour1 == 12:
            hour1 = 0

        if ampm2 == 'PM' and hour2 != 12:
            hour2 += 12
        elif ampm2 == 'AM' and hour2 == 12:
            hour2 = 0

        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    else:
        raise ValueError("Invalid input format")

if __name__ == "__main__":
    main()

def convert(time):
    hour, minute = time.split(':')
    hour = int(hour)
    minute = int(minute)
    time_converted = hour + minute / 60
    return time_converted


def main():
    time = input("Enter the time (HH:MM): ")
    time_converted = convert(time)

    if 7 <= time_converted <= 8:
        print("breakfast time")
    elif 12 <= time_converted <= 13:
        print("lunch time")
    elif 18 <= time_converted <= 19:
        print("dinner time")


if __name__ == "__main__":
    main()


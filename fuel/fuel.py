
def getvolume():

    while True:
        try:
            a = input('give me the fraction')
            x = int(a.split('/')[0])
            y = int(a.split('/')[1])
            fuel = x / y

        except (ValueError, ZeroDivisionError):
            print('something is not right')

        else:
            if fuel > 1:
                print('the number is too large')
            else:
                return fuel


def main():
    volume = getvolume()
    if volume <= 0.01:
        print('E')
    elif volume >= 0.99:
        print('F')
    else:
        print(f"{volume*100:.0f}%")

main()
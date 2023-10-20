def convert(a):
     while True:
        try:
            x = int(a.split('/')[0])
            y = int(a.split('/')[1])
            fuel = x / y
        except (ValueError, ZeroDivisionError):
            print("error")
            break
        else:
             if fuel > 1:
                return ValueError
             else:
                 return int(fuel*100)

def gauge(cf):
    if cf <= 1:
        print('E')
    elif cf >= 99:
        print('F')
    else:
        print(f"{cf:.0f}%")


def main():
    a = input('give me the fraction')
    cf = convert(a)
    gauge(cf)

if __name__ == '__main__':
    main()
import random

def getnumber():
    while True:
        try:
            a = int(input('Level: '))
            if a > 0:
                b = random.randint(1, a)
                return b
            else:
                print("Please enter a positive number.")
        except ValueError:
            continue

def main():
    n = getnumber()
    while True:
        try:
            g = int(input('Guess: '))
            if g > 0:
                if g < n:
                    print('Too small!')
                elif g > n:
                    print('Too large!')
                else:
                    print('Just right!')
            else:
                print("Please enter a positive number.")
        except ValueError:
            continue

main()
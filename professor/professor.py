import random

def main():
    l  = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        for j in range(3):
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer == x + y:
                    score = score + 1
                    break
                else:
                    print('EEE')
            except ValueError:
                continue
    print(score)



def get_level():
    while True:
        try:
            level = int(input('level: '))
            if 0< level <= 3:
                return level
            else:
                continue
        except ValueError:
                continue

def generate_integer(level):
    if level == 1:
        randomnum = random.randint(10**(level-1)-1, 10**level-1)
    else:
        randomnum = random.randint(10**(level-1), 10**level-1)
    return randomnum

if __name__ == "__main__":
    main()


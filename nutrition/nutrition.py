calorie = {
    'apple':130,
    'avocado':50,
    'sweet cherries':100,
    'kiwifruit' : 90,
    'pear':100
    }

def caloriesearch(f):
    c = calorie[f]
    return c

def main():
    f = input('type in your fruit').lower()
    if f in calorie:
        answer = caloriesearch(f)
        print(answer)

main()

def camel_to_snake(name):
    snake_case = ''
    for i in name:
        if i.isupper():
            snake_case = snake_case + '_' + i.lower()
        else:
            snake_case = snake_case + i
    return snake_case.lstrip('_')

def main():
    name = input('what is your name in camel case')
    output = camel_to_snake(name)
    print(output)

main()
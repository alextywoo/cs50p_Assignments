from validator_collection import validators, checkers, errors

def main():
    validate(input('Email: '))

def validate(s):
    try:
        validators.email(s)
        print('Valid')
    except ValueError:
        print('Invalid')

if __name__ == '__main__':
    main()


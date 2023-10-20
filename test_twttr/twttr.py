def shorten(text):
    vowels = 'AEIOUaeiou'
    return ''.join(char for char in text if char not in vowels)

def main():
    user_input = input("Enter a string of text: ")
    result = shorten(user_input)
    print(result)

if __name__ == "__main__":
    main()

def convert(x):
    x = x.replace(":)", "🙂");
    string = x.replace(":(", "🙁")
    return string

def main():
    user = input()
    converted_content = convert(user)
    print(converted_content)

main()


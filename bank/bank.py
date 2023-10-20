user_input = input('type in your greetings')
user_input_clean = user_input.strip().lower()
if user_input_clean == "hello":
    print("$0")
elif user_input_clean[0] == "h":
    print ('$20')
else:
    print('$100')
user_input = input("what is the answer to the great question of life, the universe, and everything?")
user_input_lower = user_input.lower().strip()
match user_input_lower:
    case "42" | "forty-two" | "forty two" :
        print ('Yes')
    case _:
        print('No')

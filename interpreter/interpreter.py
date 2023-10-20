def arithmetic_interpreter():
    user_input = input("Enter an arithmetic expression (x y z): ")
    x, operator, z = user_input.split()

    x = int(x)
    z = int(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    else:
        print("Invalid operator. Please enter a valid arithmetic expression.")
        return

    print(f"Result: {result:.1f}")


# Run the arithmetic interpreter
arithmetic_interpreter()
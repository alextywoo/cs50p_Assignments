import sys

def isline_empty_comment(line):
    if line.isspace():
        return True
    elif line.strip().startswith('#'):
        return True
    else:
        return False

def count_lines_of_code(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        code_lines = 0

        for line in lines:
            if not isline_empty_comment(line):
                code_lines += 1

        return code_lines  # Add this line to return the count

    except FileNotFoundError:
        sys.exit("Error: The specified file does not exist.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')  # Fixed the quotation mark here
    if not sys.argv[1].endswith('.py'):
        sys.exit("Not a python file")

    filename = sys.argv[1]

    line_count = count_lines_of_code(filename)

    print(line_count)


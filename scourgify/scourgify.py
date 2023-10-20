import sys
import csv

def name_convert(inputfile):
    try:
        with open(inputfile, 'r', newline='') as csvfile:
            input = csv.DictReader(csvfile)
            mname = []
            for row in input:
                mname.append({'first': row['name'].split(',')[1].strip(), 'last': row['name'].split(',')[0], 'house': row['house']})
    except FileNotFoundError:
        sys.exit("Error: The specified file does not exist.")


    with open(sys.argv[2], 'w', newline='') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        for row in mname:
            writer.writerow({'first':row['first'],'last':row['last'],'house':row['house']})

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many arguments')
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    inputfile = sys.argv[1]
    name_convert(inputfile)

if __name__ == "__main__":
    main()

import sys
import csv
from tabulate import tabulate

def tab_change(filename):
    with open(filename, newline='') as csvfile:
        content = list(csv.reader(csvfile))
    return content

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many arguments')
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')

    filename = sys.argv[1]
    tab = tab_change(filename)

    return tab

if __name__ == "__main__":
    tab = main()
    headers = tab[0]
    print(headers)
    print(tabulate(tab[1:], headers, tablefmt='grid'))



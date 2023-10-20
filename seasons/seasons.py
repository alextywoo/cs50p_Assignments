from datetime import date
import datetime
import inflect
import re
import sys

# Function to calculate age in minutes
def calculate_age_in_minutes(dob):
    today = datetime.date.today()
    delta = today - dob
    return delta.days * 24 * 60

# Function to convert a number to English words
def num_to_words(num):
    p = inflect.engine()
    return p.number_to_words(num)

def main():
    # Get the user's date of birth
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

    if re.match(r'^(\d{4})-(\d{2})-(\d{2})$',dob_input):
        # Parse the user's date of birth
        dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()

        # Calculate the age in minutes
        age_in_minutes = calculate_age_in_minutes(dob)

        # Convert the age to English words
        age_words = num_to_words(age_in_minutes)

        # Print the age in English words
        print(re.sub(r' and','', age_words.capitalize()) + ' minutes')

    else:
        sys.exit('wrong format')

if __name__ == "__main__":
    main()

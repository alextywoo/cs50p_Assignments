
def dollars_to_float(d):
    d = d.replace('$','')
    d = round(float(d),1)
    return d

def percent_to_float(p):
    p = p.replace('%','')
    p = round(float(p)/100,2)
    return p

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()
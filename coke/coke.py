def insert_amount(coin):
    global balance
    if coin in [25, 10, 5]:
        balance = balance + coin
    return balance

def main():
    global amount_due
    while amount_due > 0:
        insert = int(input('insert your coin: '))
        amount_due = 50 - insert_amount(insert)
        print('Amount Due:', amount_due)

    print('Change Owed:', abs(amount_due))


amount_due = 50
balance = 0
main()




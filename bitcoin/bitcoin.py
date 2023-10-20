import requests
import sys
import json


def getnumber():
    if len(sys.argv) == 1:
        sys.exit("missing command")
    elif len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            return n
        except ValueError:
            sys.exit("enter a number")
    else:
        sys.exit("something is wrong")


def get_price():
    try:
        bitjson = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = json.loads(
            bitjson.text
        )  # Use bitjson.text to get the JSON-formatted string
        price = data["bpi"]["USD"]["rate_float"]
        return price
    except requests.RequestException:
        sys.exit("Request is wrong")


def main():
    number = getnumber()
    price = get_price()
    total = price * number
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()

import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    ip_address_pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    ip_address_pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    ip_address_pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    ip_address_pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.search(ip_address_pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
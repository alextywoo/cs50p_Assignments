from seasons import main
import sys
from datetime import date
import datetime

def test():
    test_main()

def test_main():
    assert main("2022-09-15") == "Five hundred twenty-five thousand, six hundred minutes"
    assert main("2021-09-15") == "One million, fifty-one thousand, two hundred minutes"
    assert main("July-01-2023") == sys.exit


test()


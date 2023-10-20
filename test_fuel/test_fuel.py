from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert_L()
    test_convert_0()
    test_gauge_E()
    test_gauge_F()

def test_convert_L():
    assert convert('1/2') == 50
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_0():
    assert convert('0/2') == 0
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge_E():
    assert gauge(1) == 'E'
    assert gauge(2) == '2%'

def test_gauge_F():
    assert gauge(99) == 'F'
    assert gauge(98) == '98%'

if __name__ == "__main__":
    main()

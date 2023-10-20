import re
import pandas as pd
import matplotlib.pyplot as plt
from project import is_valid_location, fetch_nearest_metro_region, get_value

def test_is_valid_location():
    assert is_valid_location('Seattle, WA') == True
    assert is_valid_location('Seattle') == False
    assert is_valid_location('Atlanta, GA') == True
    assert is_valid_location('Atlanta, WA') == True
    assert is_valid_location(' ') == False

def test_fetch_nearest_metro_region():
    assert fetch_nearest_metro_region('Seattle, WA') == 'Seattle, WA'
    assert fetch_nearest_metro_region('Atlanta, GA') == 'Atlanta, GA'
    assert fetch_nearest_metro_region('Los Angeles, CA') == 'Los Angeles, CA'

def test_get_value():
    assert 706085 <= get_value('Seattle, WA') <= 706086
    assert 373493 <= get_value('Atlanta, GA') <= 373494
    assert 891327 <= get_value('Los Angeles, CA') <= 891328

from working import convert

def main():
    test_working()

def test_working():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    try:
        convert("9:16 AM 5:16 PM")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError, but no exception was raised."

    try:
        convert("9:60 AM to 5:60 PM")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError, but no exception was raised."




if __name__ == "__main__":
    main()
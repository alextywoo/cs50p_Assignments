from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("history") == "hstry"
    assert shorten("his00tory") == "hs00try"
    assert shorten("HISTORY") == "HSTRY"
    assert shorten("HISTORY, CLASS") == "HSTRY, CLSS"



if __name__ == "__main__":
    main()

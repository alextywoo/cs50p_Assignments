from bank import value

def main():
    test_firstletter()
    test_hello()
    test_other()

def test_firstletter():
    assert value('hero') == 20

def test_hello():
    assert value ('hello, madam') == 0

def test_other():
    assert value('lol') == 100

def test_case():
    assert value('HELLO') == 0

if __name__ == '__main__':
    main()
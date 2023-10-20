from plates import is_valid

def main():
    test_isalnum()
    test_numstart()
    test_numend()
    test_cap()
    test_length()
    test_punc()


def test_isalnum():
    assert is_valid('ab11dc') == False
    assert is_valid('a11bc') == False
    assert is_valid('abc12') == True

def test_numstart():
    assert is_valid('12abdc') == False
    assert is_valid('#4') == False
    assert is_valid('02abdc') == False
    assert is_valid('_2abdc') == False


def test_numend():
    assert is_valid('ab') == True
    assert is_valid('abcd12') == True
    assert is_valid('abcd02') == False
    assert is_valid('ab12cd') == False


def test_cap():
    assert is_valid('ABCDE') == True
    assert is_valid('ABcDE') == True

def test_length():
    assert is_valid('aa') == True
    assert is_valid('a') == False
    assert is_valid('aaaaaaa') == False
    assert is_valid('aaaaaa') == True

def test_punc():
    assert is_valid('AB,CD') == False
    assert is_valid('AB DE') == False



if __name__ == '__main__':
    main()
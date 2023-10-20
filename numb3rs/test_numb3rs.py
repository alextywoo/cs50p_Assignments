from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("256.1.1.1") == False
    assert validate("112567") == False
    assert validate("1.1.256") == False
    assert validate("as.1.255.255") == False
    assert validate("255.1.1.1.255") == False
    assert validate("255.1.1.1") == True




if __name__ == "__main__":
    main()
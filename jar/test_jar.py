from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    try:
        jar.deposit(13)
        assert False  # This line should not be reached if the ValueError is raised
    except ValueError:
        pass  # The ValueError is expected




def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    jar.withdraw(1)
    assert jar.size == 0
    try:
        jar.withdraw(7)
        assert False  # This line should not be reached if the ValueError is raised
    except ValueError:
        pass  # The ValueError is expected

from plates import is_valid

def test_range():
    assert is_valid('AB') == True
    assert is_valid('ABC350') == True
    assert is_valid('ABC12345') == False

def test_all_alpha():
    assert is_valid('ABCDEF') == True

def test_alnum():
    assert is_valid('CS50') == True
    assert is_valid('ABC350') == True
    assert is_valid('ABC,45') == False

def test_start():
    assert is_valid('123GAB') == False
    assert is_valid('ABC350') == True
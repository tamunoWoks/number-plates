from plates import is_valid

def test_range():
    assert is_valid('AB') == True
    assert is_valid('ABC350') == True
    assert is_valid('ABC12345') == False
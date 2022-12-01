import pytest

from expression import Expression


def test_empty_sequence():
    se = ""
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence1():
    se = "1"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence2():
    se = "1+1"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence3():
    se = "1+1+1"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence4():
    se = "(1+1)"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence5():
    se = "(22-1)*6"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence6():
    se = "(1+1)^15"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence7():
    se = "10+(15/20)"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence8():
    se = "((1+100^8))^40"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence9():
    se = "(1)+1"
    expression = Expression(se)
    assert str(expression) == se


def test_valid_sequence10():
    se = ".1"
    expression = Expression(se)
    assert str(expression) == "0.1"


def test_valid_sequence11():
    se = "15   33 + (.42 424 /2)"
    expression = Expression(se)
    assert str(expression) == "1533+(0.42424/2)"


def test_valid_sequence11():
    se = "15   33 + (.42 424 /2)"
    expression = Expression(se)
    assert str(expression) == "1533+(0.42424/2)"


def test_invalid_sequence1():
    se = "*10+2"
    with pytest.raises(ValueError):
        Expression(se)


def test_invalid_sequence2():
    se = "10(19)"
    with pytest.raises(ValueError):
        Expression(se)


def test_invalid_sequence3():
    se = "10+1+"
    with pytest.raises(ValueError):
        Expression(se)


def test_invalid_sequence4():
    se = "100.00.0"
    with pytest.raises(ValueError):
        Expression(se)


def test_invalid_sequence5():
    se = "10++19"
    with pytest.raises(ValueError):
        Expression(se)


def test_invalid_sequence6():
    se = "10(31+21)"
    with pytest.raises(ValueError):
        Expression(se)


def test_invalid_sequence7():
    se = "a"
    with pytest.raises(ValueError):
        Expression(se)

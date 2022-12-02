import pytest

from calculator import PostfixTranslator, Calculator
from expression import Expression


class TestTranslation:
    def test_valid_expression1(self):
        se = ""
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == []

    def test_valid_expression2(self):
        se = "1"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == ["1"]

    def test_valid_expression3(self):
        se = "1+1"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == ["1", "1", "+"]

    def test_valid_expression4(self):
        se = "10+20+30"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == ["10", "20", "+", "30", "+"]

    def test_valid_expression5(self):
        se = "10+20*30"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == ["10", "20", "30", "*", "+"]

    def test_valid_expression6(self):
        se = "(10+20)*30"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == ["10", "20", "+", "30", "*"]

    def test_valid_expression7(self):
        se = "(10+20)*30^4/100"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == [
            "10",
            "20",
            "+",
            "30",
            "4",
            "^",
            "*",
            "100",
            "/",
        ]

    def test_valid_expression8(self):
        se = "(10+20)*30^(4/100)"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        trans.make_postfix()
        assert trans.postfix == [
            "10",
            "20",
            "+",
            "30",
            "4",
            "100",
            "/",
            "^",
            "*",
        ]

    def test_invalid_expression1(self):
        se = "(1+1"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        with pytest.raises(ValueError):
            trans.make_postfix()

    def test_invalid_expression2(self):
        se = "(1"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        with pytest.raises(ValueError):
            trans.make_postfix()

    def test_invalid_expression3(self):
        se = "(1+(1+1)))"
        trans = PostfixTranslator()
        trans.set_expression(Expression(se))
        with pytest.raises(ValueError):
            trans.make_postfix()

    def test_str(self):
        se = "1+1"
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        assert str(calc) == "1 1 +"

    def test_repr(self):
        se = "1+1"
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        assert repr(calc) == "Expression: 1+1# | Postfix: ['1', '1', '+']"


class TestCalculation:
    def test_super_method(self):
        se = "(1+1)"
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        assert calc.postfix == ["1", "1", "+"]

    def test_calculation1(self):
        se = "(1+1)"
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        calc.calculate()
        assert calc.result == 2

    def test_calculation2(self):
        se = ""
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        calc.calculate()
        assert calc.result == 0

    def test_calculation3(self):
        se = "1"
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        calc.calculate()
        assert calc.get_result() == 1

    def test_calculation4(self):
        se = "(3-1)*2"
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        calc.calculate()
        assert calc.result == 4

    def test_calculation5(self):
        se = "1+(50-100)/300^(10%3)"
        calc = Calculator()
        calc.set_expression(Expression(se))
        calc.make_postfix()
        calc.calculate()
        assert pytest.approx(float(calc.result), 0.0001) == 0.8333

    def test_no_expressin_postfix(self):
        calc = Calculator()
        calc.make_postfix()
        assert calc.postfix == []

    def test_no_expressin_calculate(self):
        calc = Calculator()
        calc.make_postfix()
        calc.calculate()
        assert calc.get_result() == 0

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui import Ui_MainWindow
from operators import *
from expression import Expression
from calculator import Calculator


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super(CalculatorWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Input buttons events
        self.ui.btn_0.clicked.connect(lambda: self.add_symbol("0"))
        self.ui.btn_1.clicked.connect(lambda: self.add_symbol("1"))
        self.ui.btn_2.clicked.connect(lambda: self.add_symbol("2"))
        self.ui.btn_3.clicked.connect(lambda: self.add_symbol("3"))
        self.ui.btn_4.clicked.connect(lambda: self.add_symbol("4"))
        self.ui.btn_5.clicked.connect(lambda: self.add_symbol("5"))
        self.ui.btn_6.clicked.connect(lambda: self.add_symbol("6"))
        self.ui.btn_7.clicked.connect(lambda: self.add_symbol("7"))
        self.ui.btn_8.clicked.connect(lambda: self.add_symbol("8"))
        self.ui.btn_9.clicked.connect(lambda: self.add_symbol("9"))
        self.ui.btn_lbracket.clicked.connect(lambda: self.add_symbol(LBRACKET))
        self.ui.btn_rbracket.clicked.connect(lambda: self.add_symbol(RBRACKET))
        self.ui.btn_dot.clicked.connect(lambda: self.add_symbol("."))
        self.ui.btn_plus.clicked.connect(lambda: self.add_symbol(PLUS))
        self.ui.btn_minus.clicked.connect(lambda: self.add_symbol(MINUS))
        self.ui.btn_mul.clicked.connect(lambda: self.add_symbol(MUL))
        self.ui.btn_div.clicked.connect(lambda: self.add_symbol(DIV))
        self.ui.btn_exp.clicked.connect(lambda: self.add_symbol(EXP))
        self.ui.btn_mod.clicked.connect(lambda: self.add_symbol(MOD))

        # Control button events
        self.ui.btn_escape.clicked.connect(self.escape)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_equal.clicked.connect(self.caluculate)

        # Calculator objects
        self.calc = Calculator()

    def add_symbol(self, btn_text: str) -> None:
        """Add a symbol (digit/operator) to the input edit line."""
        cur_pos = self.ui.le_input.cursorPosition()
        input_text = self.ui.le_input.text()
        if input_text == "0" and btn_text != ".":
            self.ui.le_input.setText(btn_text)
        else:
            self.ui.le_input.setText(
                input_text[:cur_pos] + btn_text + input_text[cur_pos:]
            )
            self.ui.le_input.setCursorPosition(cur_pos + 1)
            self.ui.le_input.setFocus()

    def escape(self):
        """Delete a symbol of the edit line."""
        cur_pos = self.ui.le_input.cursorPosition() - 1
        input_text = self.ui.le_input.text()
        if len(input_text) == 1:
            self.ui.le_input.setText("0")
        elif cur_pos != -1:
            self.ui.le_input.setText(
                input_text[:cur_pos] + input_text[cur_pos + 1 :]
            )
            self.ui.le_input.setCursorPosition(cur_pos)
            self.ui.le_input.setFocus()

    def clear(self):
        self.ui.le_input.setText("0")
        self.ui.lbl_output.clear()

    def caluculate(self):
        """Calculate expression from the edit line, put result in the output."""
        inp = self.ui.le_input.text()
        try:
            expression = Expression(inp)
        except ValueError:
            self.ui.lbl_output.setText("Invalid expression.")
            return
        self.ui.le_input.setText(str(expression))
        self.calc.set_expression(expression)
        try:
            self.calc.make_postfix()
            self.calc.calculate()
        except ValueError:
            self.ui.lbl_output.setText("Calculation error.")
        except ZeroDivisionError:
            self.ui.lbl_output.setText("Calculation error: division by 0.")
            return
        self.ui.lbl_output.setText(f"= {self.calc.get_result()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()

    sys.exit(app.exec())

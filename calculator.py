from collections import deque
from decimal import Decimal

from operators import *
from expression import Expression


# Control table for postfix translation algorithm
# See readable version in README.md
# |   | # | ( | + | - | * | / | ) | ^ | % |
# | # | 6 | 1 | 1 | 1 | 1 | 1 | 5 | 1 | 1 |
# | ( | 5 | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 |
# | + | 4 | 1 | 2 | 2 | 1 | 1 | 4 | 1 | 1 |
# | - | 4 | 1 | 2 | 2 | 1 | 1 | 4 | 1 | 1 |
# | * | 4 | 1 | 4 | 4 | 2 | 2 | 4 | 1 | 2 |
# | / | 4 | 1 | 4 | 4 | 2 | 2 | 4 | 1 | 2 |
# | ^ | 4 | 1 | 4 | 4 | 4 | 4 | 4 | 1 | 4 |
# | % | 4 | 1 | 4 | 4 | 2 | 2 | 4 | 1 | 2 |
CONTROL_TABLE = {
    END: {
        END: "6",
        LBRACKET: "5",
        PLUS: "4",
        MINUS: "4",
        MUL: "4",
        DIV: "4",
        EXP: "4",
        MOD: "4",
    },
    LBRACKET: {
        END: "1",
        LBRACKET: "1",
        PLUS: "1",
        MINUS: "1",
        MUL: "1",
        DIV: "1",
        EXP: "1",
        MOD: "1",
    },
    RBRACKET: {
        END: "5",
        LBRACKET: "3",
        PLUS: "4",
        MINUS: "4",
        MUL: "4",
        DIV: "4",
        EXP: "4",
        MOD: "4",
    },
    PLUS: {
        END: "1",
        LBRACKET: "1",
        PLUS: "2",
        MINUS: "2",
        MUL: "4",
        DIV: "4",
        EXP: "4",
        MOD: "4",
    },
    MINUS: {
        END: "1",
        LBRACKET: "1",
        PLUS: "2",
        MINUS: "2",
        MUL: "4",
        DIV: "4",
        EXP: "4",
        MOD: "4",
    },
    MUL: {
        END: "1",
        LBRACKET: "1",
        PLUS: "1",
        MINUS: "1",
        MUL: "2",
        DIV: "2",
        EXP: "4",
        MOD: "2",
    },
    DIV: {
        END: "1",
        LBRACKET: "1",
        PLUS: "1",
        MINUS: "1",
        MUL: "2",
        DIV: "2",
        EXP: "4",
        MOD: "2",
    },
    EXP: {
        END: "1",
        LBRACKET: "1",
        PLUS: "1",
        MINUS: "1",
        MUL: "1",
        DIV: "1",
        EXP: "1",
        MOD: "1",
    },
    MOD: {
        END: "1",
        LBRACKET: "1",
        PLUS: "1",
        MINUS: "1",
        MUL: "2",
        DIV: "2",
        EXP: "4",
        MOD: "2",
    },
}


class PostfixTranslator:
    """Translate infix math expression to postfix notation.

    Calculations of a math expression use the postfix notation. This class
    translates an infix math expression to postfix. The control table set
    rules of translation. Translation chooses operation functions by the table
    (`oper[n]`). Translation uses 2 stacks, pointer and puts the result postfix
    expression in `postfix`.
    More about postfix notation: https://www.cs.man.ac.uk/~pjj/cs212/fix.html

    Example:
        infix: (A+B)*C-D
        postfix: AB+C*D-

    Attrs:
        stack: stores operators while translation.
        postfix: the result postfix expression.
        expression: an `Expression` instance (input infix math expression).
        pointer: pointer (index number) to an expression.

    Raises:
        ValueError: bad sequence (the control table decides).

    """

    def __init__(self):
        self.stack: deque = deque(END)
        self.postfix: list = []
        self.expression: Exception = None
        self.pointer: int = 0

    def _clear(self):
        self.__init__()

    def set_expression(self, expression: Expression):
        self._clear()
        self.expression = expression

    def make_postfix(self):
        """Translate `expression` to `postfix`."""
        self.postfix = []
        self.pointer = 0
        if not self.expression:
            return
        expression = self.expression.value
        expression += END
        while True:
            token = expression[self.pointer]
            if token[0].isdigit():
                self.postfix.append(token)
                self.pointer += 1
                continue
            # Choose an operation
            operation_code = CONTROL_TABLE[token][self.stack[-1]]
            # Run operation (end of transltaion returns True)
            if self.operate(operation_code, token):
                break
        self.stack = deque(END)

    def oper1(self, token: str) -> bool:
        self.stack.append(token)
        self.pointer += 1
        return False

    def oper2(self, token: str) -> bool:
        self.postfix.append(self.stack.pop())
        self.stack.append(token)
        self.pointer += 1
        return False

    def oper3(self, token: str) -> bool:
        self.stack.pop()
        self.pointer += 1
        return False

    def oper4(self, token: str) -> bool:
        self.postfix.append(self.stack.pop())
        return False

    def oper5(self, token: str):
        raise ValueError(f"Translation erorr on `{token}` token.")

    def oper6(self, token: str) -> bool:
        """End translation."""
        return True

    def operate(self, code: str, token: str) -> bool:
        """Choose an operation function by the operation code.

        Args:
            code: a code of a operation function.
            token: a expression token (digit/operator/sys symbol).
        Returns:
            Result of an operation function. The `end` operation function
            returns True, rest of them resturn False.
        """
        operation_map = {
            "1": self.oper1,
            "2": self.oper2,
            "3": self.oper3,
            "4": self.oper4,
            "5": self.oper5,
            "6": self.oper6,
        }
        operation_function = operation_map[code]
        return operation_function(token)

    def __str__(self):
        return " ".join(self.postfix)

    def __repr__(self):
        return " ".join(
            [
                "Expression:",
                str(self.expression),
                "|",
                "Postfix:",
                str(self.postfix),
            ]
        )


class Calculator(PostfixTranslator):
    """Calculate result based on translated postfix expression.

    Calculation uses `num_stuck` and `postfix` and puts the result in `result`.

    Attrs:
        stack: stores numbers while calculation.
        result: the result number of calclulations.
        ...
    """

    def __init__(self):
        self.result = 0
        super().__init__()

    def _prepare_postfix(self):
        if not self.postfix:
            self.result = 0
            return
        self.postfix.append(END)

    def clear(self):
        self.result = 0
        self.stack = deque(END)

    def _calc_result(self, left: str, right: str, operator: str) -> Decimal:
        left = Decimal(left)
        right = Decimal(right)
        if operator == PLUS:
            return left + right
        elif operator == MINUS:
            return left - right
        elif operator == MUL:
            return left * right
        elif operator == DIV:
            return left / right
        elif operator == EXP:
            return left**right
        elif operator == MOD:
            return left % right
        else:
            raise ValueError(f"Wrong operator - `{operator}`.")

    def calculate(self):
        self._prepare_postfix()
        self.clear()
        postfix = self.postfix
        for token in postfix:

            if token[0].isdigit():
                self.stack.append(token)

            elif token != END:
                right = self.stack.pop()
                left = self.stack.pop()
                res = self._calc_result(left, right, token)
                self.stack.append(res)

            elif token == END:
                self.result = Decimal(self.stack.pop())

            else:
                raise ValueError(f"Wrong token - `{token}`.")

    def get_result(self) -> Decimal:
        return self.result

from collections import deque

from operators import *
from expression import Expression


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
    def __init__(self):
        self.num_stack = deque(END)
        self.opr_stack = deque(END)
        self.postfix = []
        self.expression = None
        self.pointer = 0
        super().__init__()

    def _clear(self):
        self.__init__()

    def set_expression(self, expression: Expression):
        self._clear()
        self.expression = expression

    def make_postfix(self):
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
            operation_code = CONTROL_TABLE[token][self.opr_stack[-1]]
            if self.operate(operation_code, token):
                break
        self.num_stack = deque(END)
        self.opr_stack = deque(END)

    def oper1(self, token):
        self.opr_stack.append(token)
        self.pointer += 1
        return False

    def oper2(self, token):
        self.postfix.append(self.opr_stack.pop())
        self.opr_stack.append(token)
        self.pointer += 1
        return False

    def oper3(self, token):
        self.opr_stack.pop()
        self.pointer += 1
        return False

    def oper4(self, token):
        self.postfix.append(self.opr_stack.pop())
        return False

    def oper5(self, token):
        raise ValueError(f"Translation erorr on `{token}` token.")

    def oper6(self, token):
        return True

    def operate(self, code, token):
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
        return str(
            "Expression:", self.expression, "|", "Postfix:", self.postfix
        )


class Calculator(PostfixTranslator):
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
        self.num_stack = deque(END)
        self.opr_stack = deque(END)

    def _calc_result(self, left, right, operator):
        left = float(left)
        right = float(right)
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
                self.num_stack.append(token)

            elif token != END:
                right = self.num_stack.pop()
                left = self.num_stack.pop()
                res = self._calc_result(left, right, token)
                self.num_stack.append(res)

            elif token == END:
                self.result = float(self.num_stack.pop())

            else:
                raise ValueError(f"Wrong token - `{token}`.")

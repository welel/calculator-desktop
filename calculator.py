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


class Calculator:
    def __init__(self):
        self.expression = None
        self.postfix = []
        self.num_stack = deque(END)
        self.opr_stack = deque(END)
        self.pointer = 0
        self.error = ""

    def clear(self):
        self.__init__()

    def set_expression(self, expression: Expression):
        self.clear()
        self.expression = expression

    def make_postfix(self):
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
            print(token, self.postfix, self.opr_stack)
            operation_code = CONTROL_TABLE[token][self.opr_stack[-1]]
            if self.operate(operation_code, token):
                break

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
        self.error = f"Translation erorr on `{token}` token."
        return True

    def oper6(self, token):
        print("END")
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
        return "\n".join(
            [
                str(self.expression),
                str(self.postfix),
                str(self.num_stack),
                str(self.opr_stack),
                str(self.pointer),
                str(self.error),
            ]
        )

__all__ = [
    "LBRACKET",
    "RBRACKET",
    "PLUS",
    "MINUS",
    "MUL",
    "DIV",
    "EXP",
    "MOD",
    "END",
    "START",
    "BRAKETS",
    "MATH_SIGNS",
    "OPERATORS",
]

LBRACKET = "("
RBRACKET = ")"
PLUS = "+"
MINUS = "-"
MUL = "*"
DIV = "/"
EXP = "^"
MOD = "%"
END = "#"
START = "$"
BRAKETS = (LBRACKET, RBRACKET)
MATH_SIGNS = (PLUS, MINUS, MUL, DIV, EXP, MOD)
OPERATORS = tuple(BRAKETS + MATH_SIGNS)
SERVICE_SYMBOLS = (START, END)

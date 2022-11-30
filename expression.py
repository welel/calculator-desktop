from operators import *


class Expression:
    """Parse a string math expression to the list and validate it.

    Token - operator / math sign / bracket / service symbol.

    Attrs:
        value (list): a sequesnce of parsed tokens.
        _num_builder (list): a temp storage for parsing.
    Raises:
        ValueError - if validation is failed.

    Validation guarantees:
        - value has only digits and `OPERATORS`;
        - value doesn't have numbers with 2 dots;
        - every single element of the value either number or operator;
        - value doesn't start and end with math sign;
        - 2 math signs can't be next to each other.
    """

    def __init__(self, expression: str):
        self.value = [START]
        self._num_builder = []
        self._parse(expression)

    def _parse(self, expression):
        expression = expression.replace(" ", "") + END
        for symbol in expression:
            self.add(symbol)
        self.add(END)
        self.value = self.value[1:]

    def _build_number(self):
        if not self._num_builder:
            return

        number = "".join(self._num_builder)
        if number.count(".") > 1:
            raise ValueError("Number has more that one dot.")

        number = number.lstrip("0").rstrip(".")
        number = number if number[0] != "." else "0" + number

        if self.value[-1] == RBRACKET:
            raise ValueError("Invalid sequence.")

        self.value.append(number)
        self._num_builder = []

    def add(self, symbol):
        if not (symbol.isdigit() or symbol == "."):
            self._build_number()

        if symbol in MATH_SIGNS:
            last = self.value[-1]
            if last in [LBRACKET, START] or last in MATH_SIGNS:
                raise ValueError("Invalid sequence.")
            self.value.append(symbol)

        elif symbol in BRAKETS:
            last = self.value[-1]
            if symbol == LBRACKET and (last[0].isdigit() or last == RBRACKET):
                raise ValueError("Invalid sequence.")
            elif symbol == RBRACKET and (
                last in MATH_SIGNS or last in [LBRACKET, START]
            ):
                raise ValueError("Invalid sequence.")
            self.value.append(symbol)

        elif symbol.isdigit() or symbol == ".":
            last = self.value[-1]
            if last == RBRACKET:
                raise ValueError("Invalid sequence.")
            self._num_builder.append(symbol)

        elif symbol == END:
            last = self.value[-1]
            if last in MATH_SIGNS or last == LBRACKET:
                raise ValueError("Invalid sequence.")
            elif last[0].isdigit() and self.value[-2] == RBRACKET:
                raise ValueError("Invalid sequence.")
        else:
            raise ValueError("Bad symbol.")

    def __str__(self):
        return "".join(self.value)

    def __repr__(self):
        return str(self.value)

class ExpressionTypeError(Exception):
    def __init__(self, line_number, operation_value, type1_name, type2_name=None):
        super().__init__()


class NonDeclaredVariableError(Exception):
    def __init__(self, line_number, identifier_name):
        super().__init__()


class UnexpectedTypeError(Exception):
    def __init__(self, line_number: int, expected_type, received_type):
        super().__init__()


class BreakException(Exception):
    def __init__(self, line_number: int):
        super().__init__()


class ReturnException(Exception):
    def __init__(self, line_number: int):
        super().__init__()


class MissingArgument(Exception):
    def __init__(self, line: int, expected_args_num: int, received_args_num: int):
        super().__init__()


class UndeclaredFunction(Exception):
    def __init__(self, line_number: int, identifier_name: str):
        super().__init__()


class AlreadyDeclaredError(Exception):
    def __init__(self, line_number: int, identifier_name: str):
        super().__init__()

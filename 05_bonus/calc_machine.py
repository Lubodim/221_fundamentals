def calc(num_1, num_2, operator):
    if operator in ["/", "//", "%"] and num_2 == 0:
        return f"Second number '{num_2}' must be different from ZERO! Tyr again"

    my_calc = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "**": lambda x, y: x ** y,
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "%": lambda x, y: x % y,
    }
    result = my_calc[operator](num_1, num_2)
    return f"{num_1} {operator} {num_2} = {result}"


def add(num_1, num_2, operator):
    if operator == '+':
        return f"{num_1} {operator} {num_2} = {num_1 + num_2}"


def subtract(num_1, num_2, operator):
    if operator == '-':
        return f"{num_1} {operator} {num_2} = {num_1 - num_2}"



def multiplication(num_1, num_2, operator):
    if operator == '*':
        return f"{num_1} {operator} {num_2} = {num_1 * num_2}"


def grading(num_1, num_2):
    return num_1 ** num_2
def divide(num_1, num_2):
    return num_1 / num_2

def integer_divide(num_1, num_2):
    return num_1 // num_2


def modulo_divide(num_1, num_2):
    return num_1 % num_2

def calc_2(num_1, num_2, operator):
    my_calc = {
        "+": add(num_1, num_2),
        "-": subtract(num_1, num_2),
        "*": multiplication(num_1, num_2),
        "**": grading(num_1, num_2),
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "%": lambda x, y: x % y,
    }
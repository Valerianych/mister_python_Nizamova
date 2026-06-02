def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    result = a / b
    return result


def is_even(number):
    result = number % 2 == 0
    return result

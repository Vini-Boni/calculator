def addition(*args):
    if len(args) < 2:
        raise ValueError("Pelo menos dois argumentos são necessários para a adição.")
    result = args[0]
    for num in args[1:]:
        result += num
    return result


def subtraction(*args):
    if len(args) < 2:
        raise ValueError("Pelo menos dois argumentos são necessários para a subtração.")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiplication(*args):
    if len(args) < 2:
        raise ValueError(
            "Pelo menos dois argumentos são necessários para a multiplicação."
        )
    result = args[0]
    for num in args[1:]:
        result *= num
    return result


def division(*args):
    if len(args) != 2:
        raise ValueError("Somente dois argumentos são esperados para a divisão.")
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

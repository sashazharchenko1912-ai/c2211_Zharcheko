import math

def safe_calculator(func):
    def wrapper(expression):
        try:
            if not isinstance(expression, str):
                raise ValueError("Вираз має бути рядком")

            allowed_symbols = "0123456789+-*/(). "
            for char in expression:
                if char not in allowed_symbols:
                    raise ValueError("Заборонений символ у виразі")

            result = func(expression)
            return result

        except ZeroDivisionError:
            return "Помилка: ділення на нуль"
        except Exception as e:
            return f"Помилка: {e}"

    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)


if __name__ == "__main__":
    print(calculate("2 + 3 * 4"))
    print(calculate("10 / 0"))
    print(calculate("2 + abc"))

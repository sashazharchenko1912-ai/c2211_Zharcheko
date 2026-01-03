def checker(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except Exception as exc:
        print(f"We have problems{exc}")
    else:
        print(f"No problems. Result - {result}")
    return checker


def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
calculate(2+2)
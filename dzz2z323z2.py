result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for k in data:
    try:
        result.append(divider(k, data[k]))
    except Exception as e:
        print(type(e).__name__)

print(result)

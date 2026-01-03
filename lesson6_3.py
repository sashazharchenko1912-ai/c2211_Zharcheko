try:
    print("start code")
    print(10/0)
    print("No error")
except (NameError,ZeroDivisionError):
    print("We have Error")


print("Code after capsule")
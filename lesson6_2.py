try:
    print("start code")
    print(10/0)
    print("No error")
except NameError:
    print("We have NameError")
except ZeroDivisionError:
    print("We have an ZeroDivisionError")

print("Code after capsule")
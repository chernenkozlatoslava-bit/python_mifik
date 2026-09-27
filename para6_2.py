try:
    print("start code")
    print(10/0)
    print("no error")
except NameError:
    print("We have a Name error!")
except ZeroDivisionError:
    print("We have a ZeroDivision error!")

print("Code after capsule")

class ForbiddenNumberError(Exception):

    def __str__(self):
        return "Number is banned"


def check(number):
    if "13" in str(number):
        raise ForbiddenNumberError()
    else:
        return "Number is OK"

try:
    num = input("Enter number ")
    res = check(num)
    print(res)
except ForbiddenNumberError as er:
    print(er)
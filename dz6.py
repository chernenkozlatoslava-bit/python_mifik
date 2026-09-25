result = []

def divider(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")


try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

except TypeError:
    print("TypeError: список [] не можна використовувати як ключ словника")
    data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}


for key in data:
    res = divider(key, data[key])
    # result.append(res)
    if res is not None:
        result.append(res)

print(result)
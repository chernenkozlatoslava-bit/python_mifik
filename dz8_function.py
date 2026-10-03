import time

def calculate():
    result = 0
    for i in range(10 * 10 ** 6):
        result += i
    return result

def measure_time(func):
    start = time.perf_counter()
    result = func()
    end = time.perf_counter()
    execution_time = end - start
    print(f"Execution time: {execution_time:.6f} seconds")
    return result

# res = calculate()
# print(res)

# if __name__ == "__main__":
measure_time(calculate)
class NumberSequence:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for number in range(self.start, self.stop + 1):
            yield number



numbers = NumberSequence(1, 5)

# First iteration
for n in numbers:
    print(n)

print("---")

# Second iteration
for n in numbers:
    print(n)

generator = iter(numbers)
print("Перші 3 елементи генератора:")
print(next(generator))
print(next(generator))
print(next(generator))
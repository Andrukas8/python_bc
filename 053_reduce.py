# reduce(function, iterable) - apply a function to an iterable and reduce it to a single cumulative value
# performs function on first two elements and repeats process until 1 value remains

import functools

letters = ["H", "E", "L", "L", "O"]

word = functools.reduce(lambda x, y: x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]

number = functools.reduce(lambda x, y: x * y, factorial)
print(number)

number_2 = functools.reduce(lambda a, b: a * b, range(1, 6))
print(number_2)

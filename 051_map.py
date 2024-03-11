# map(function, iterable) - will aply a function to each item in an iterable (list, tuple, etc.)

store = [("Shirt", 20.00), ("Pants", 25.00), ("Jacket", 50.00), ("Socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1] / 0.82)

store_EUR = list(map(to_euros, store))
store_USD = list(map(to_dollars, store_EUR))

print("EUR")
for item in store_EUR:
    print(item)

print("USD")
for item in store_USD:
    print(item)

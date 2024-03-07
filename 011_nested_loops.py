rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to cast: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("This file was not found")
    
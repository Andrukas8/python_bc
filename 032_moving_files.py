import os

source = "test.txt"
destination = "C:\\Users\\andri\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"{source} not found")

# can be used for folders too
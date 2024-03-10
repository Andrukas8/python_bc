import os
path = "C:\\Users\\andri\\Documents\\Coding\\python_bc\\test.txt"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location does not exist")
# str.format() = optional methog that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Bro"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name)) # Left
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # Right
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # Center

number = 3.14159
print("The number pi is {:.2f}".format(number)) # display first 2 digits after the decimal of the float
print("The number pi is {:,}".format(1000)) # prints 1000 as 1,000
print("The number pi is {:b}".format(1000)) # binary
print("The number pi is {:o}".format(1000)) # octanary
print("The number pi is {:X}".format(1000)) # hexadecimal
print("The number pi is {:e}".format(1000)) # scientific notation e
print("The number pi is {:E}".format(1000)) # scientific notation E
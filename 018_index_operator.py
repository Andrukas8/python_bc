# [] - index operator

name = "bro Code!"

if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[0:3]
first_name = first_name.upper()
last_name = name[4:].upper()
last_character = name[-1]
print(first_name, last_name, last_character)
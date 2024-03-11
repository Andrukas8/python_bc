# lambda function = function written in 1 line using lambda keyword accepts any number of arguments, but only has one expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: f"{first_name} {last_name}"
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(4, 5))
print(add(5, 6, 7))
print(full_name("Bro", "Code"))
print(age_check(12))
print(age_check(20))

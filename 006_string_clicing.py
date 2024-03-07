name = "Bro Code"
first_name = name[0:3]
last_name = name[4:]
funky_name = name[0:8:2]
funky_name_2 = name[::2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(funky_name_2)
print(reversed_name)

# Slice object (reusable slicing)
website1 = "https://google.com"
website2 = "https://wikipedia.com"
slice = slice(8,-4)
print(website1[slice])
print(website2[slice])
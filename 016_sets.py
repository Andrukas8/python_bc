utensils = {"fork", "spoon", "knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()

dishes = {"bowl", "plate", "cup", "knife"}

utensils.update(dishes)

print(utensils)

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))

for x in dinner_table:
    print(x)

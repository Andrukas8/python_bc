food = ["pizza", "cucumber", "apple"]
print(food)

for f in food:
    print(f)

print(food[0])

food.append("ice cream")
print(food)

food.remove("cucumber")
print(food)

print(food.pop())

food.insert(0, "cake")
print(food)

food.sort()
print(food)

food.clear()
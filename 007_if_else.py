age = int(input("How old are you?: "))

if age >= 18:
    print("you are an adult")
elif age < 0:
    print("you haven't been born yet")
else:
    print("you are a child")
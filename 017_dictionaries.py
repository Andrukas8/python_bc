capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijin",
            "Italy": "Rome"}

print(capitals["Italy"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})

capitals.pop("China")

for key, value in capitals.items():
    print(f"Capital of {key} is {value}")

capitals.clear()





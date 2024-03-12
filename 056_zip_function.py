# zip (*iterables) - aggregate elements from two or more iterables and creates a zip object with paired elements stored in tuples

usernames = ["Dude", "Bro", "Mister"]
passwords = ["p@ssword", "abc123", "guest"]

users = zip(usernames, passwords)

print(type(users)) # ziip functions

users = dict(users)

for key, value in users.items():
    print(f"{key} : {value}")

# ---------------------
usernames = ["Dude", "Bro", "Mister"]
passwords = ["p@ssword", "abc123", "guest"]
login_dates = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_dates)

for i in users: print(i)
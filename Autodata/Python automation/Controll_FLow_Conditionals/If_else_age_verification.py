theater_name = "XYZ"
Age_limit = 17

print(f" Welcome to {theater_name} theaters!!") # py3
print("Welcome to {} theaters!!!".format(theater_name))  # py2 and py3

user_input = input("Enter your age:")
print(f"User input is: {user_input}")

if int(user_input) >= Age_limit:
    print("Enjoy the movie ")
else:
    print("Your must be 17 to watch the movie")
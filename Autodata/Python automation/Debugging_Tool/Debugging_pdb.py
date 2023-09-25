"""
Official doc = https://docs.python.org

c =continue
n = next
l = show current line
s = step
h = help
pp = pretty print

"""
import pdb


# Demo-1

# import pdb
# print("I am the 1st line")
# fname = "Admas"
# lname = "kinfu"
# pdb.set_trace()  #  Breakpoint
# print("I am the 2nd line")
# print("I am 3rd line")
# print(f"First name is '{fname}' and last name is '{lname}'")

# Demo-2

def get_user_name(name):
    user_names = {"admas": "ak",
                  "joe": "joe99",
                  "mary": " marryrock2023"}
    print(f'The user "{user_names[name]}" is logged in.')
    # pdb.set_trace()

    return user_names[name]

user_1 =get_user_name("admas")
print(("User 1: " + user_1))
pdb.set_trace()

user_2 = get_user_name("joe")
print("User 2: " + user_2)
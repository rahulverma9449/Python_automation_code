# infinity loop

# my_var = True
# while my_var:
#     print('abc')

# good loop limit
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter = counter + 1

main_number = 8
user_input = 0
while user_input != main_number:
    user_input = input("Enter a number 0 to 10: ")
    user_input = int(user_input)
    print(type(user_input))
    print(f"You entered; {user_input}")
    print(user_input != main_number)


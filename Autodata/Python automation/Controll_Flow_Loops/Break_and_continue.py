# Example 1
# main_number = 15
# #user_input = 0
# while True:
#     user_input = input("Guess a number 0 to 20: ")
#     print(f"You entered; {user_input}")
#     if int(user_input) == main_number:
#         break
#     else:
#         continue
#
#
# print("Done !!!!!")

# program is for find capitals
# Example 2
# capitals = {
#     "Peru": " Lima",
#     "Philippines": "Manila",
#     "Spain": "Marid",
#     "Ethiopia": "Addis ababa",
#     "Ghana": "Accra"}
# user_input = 'Spain'
#
# for country,capital in capitals.items():
#     print("current country: " + country)
#     if user_input.lower() == country.lower():
#         print("Capitals is : " + capital)
#         break
#     else:
#         print("Unknown")
# capitals_city = capitals[user_input]


book_prices = {"calculus": 300, "Physics": 255, "Chemistry": 400,"English": 150, "Theater ticket": 100}
my_courses = ["Physics", "English","Psychology", "Calculus", "History"]
total_cost = 0
for course in my_courses:
    if course not in book_prices.keys():
        continue
    total_cost += book_prices[course]
    total_cost = total_cost + book_prices[course]
print("Total books cost: {}".format(total_cost))

# a =5
# # b =5
# # c = 30
# # d = 7
# #
# # if a < b:
# #     print(" 'a' is less than 'b'. ")
# # elif a > b :
# #     print("'a' is greater than 'b'")
# # # if d < c:
# # #     print(" 'd' is less than 'c'. ")
# # else:
# #
# #     print("equal")
user = input("Enter your favorite entertainment:   ")
shows = ["Friends", "The Office", "Breaking Bad","Stranger Things"]
movies = ["Rocky","Jaws", "Batsman", "Wonder Woman"]

my_choice = user

if my_choice in shows or my_choice in movies:
    print(f"Your choice is valid for {my_choice}")
else:
    print("Unknown")
# if my_choice in shows:
#     print("Your choice is a show.")
# elif my_choice in movies:
#     print("Your choice is a movie")
# else:
#     print("Your choice is Unknown.")
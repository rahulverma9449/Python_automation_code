# Example of using Keywords parameters
# Example 1: Write a function that will return number of words that have x length, givena string
# def get_count_of_small_words(input_string, max_size=3):
#
#     small_words = []
#     for word in input_string.split():
#         if len(word) <= max_size:
#             small_words.append(word)
#
#     return len(small_words)
# my_joke_1 = "In Python hashtags are used to tell the computer a line is not worth reading. much like social media."
#
# # num_small = get_count_of_small_words(my_joke_1)
# # num_small = get_count_of_small_words(my_joke_1, max_size= 4)
# num_small = get_count_of_small_words(my_joke_1, 4)
# print(num_small)


# Example 2

def connect_to_database(host='test.db.com', username= 'tester', password= 'tester@pass'):
    print(f"Connection to host: {host}")
    print(f"Username: {username}")

#connect_to_database()

connect_to_database(host='pad.tb.com', username= 'manage', password= 'tester@123')



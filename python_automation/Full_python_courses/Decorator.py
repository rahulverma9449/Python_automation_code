# def add_greeting(func):
#     def wrapper(*args, **kwargs):
#         print("Hello!")
#         return wrapper
# def say_hello(name):
#     print("Hello, {}!".format(name))
# say_hello("Alice")

# a = "Hello, World!"
# print(a.remove("H", "J"))


def replace(str, char1, char2):
    newstr = ""
    for char in str:
        if(char == char1):
            newstr +=char2
        else:
            newstr +=char
    return newstr
str = "ffsshhrbss"
str = replace(str,'s','d')
print(str)
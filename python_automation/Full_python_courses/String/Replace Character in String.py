# def replace(str, char1, char2):
#     newStr = ""
#     for char in str:
#         if (char == char1):
#             newStr += char2
#         else:
#             newStr += char
#     return newStr
#
# str = "gkjskasl"
# str = replace(str, 'j', 'abc')
# print(str)
def replace(str, char1, char2):
    newStr = ""
    for char in str:
        if (char == char1):
            newStr += char2
        else:
            newStr += char
    return newStr


str = "fsafsavxz"
str = replace(str, 's', 'd')
print(str)
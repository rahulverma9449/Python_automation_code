# def isPermutation(string1, string2):
#     if len(string1) != len(string2):
#         return False
#
#     # Create a dictionary to keep track of the frequency of characters in string1
#     char_frequency = {}
#
#     # Populate the dictionary
#     for char in string1:
#         if char in char_frequency:
#             char_frequency[char] += 1
#         else:
#             char_frequency[char] = 1
#
#     # Check if each character in string2 has the same frequency as in string1
#     for char in string2:
#         if char in char_frequency:
#             char_frequency[char] -= 1
#             if char_frequency[char] < 0:
#                 return False
#         else:
#             return False
#
#     return True


# def reverseEachWord(string):
#     result = ""
#     for i in range(-1):
#         string = string.reverse(i)
#     return string
#
# string = "hello"
# a = reverseEachWord(string)
# print(a)


def getCompressedString(input):
    # create an empty string to store the compressed version of the input string
    compressed_string = ""
    current_char = ""       # keep track of the current character being processed
    char_count = 0          # keep track of the number of occurrences of the current character
    for char in input:
        if char == current_char:
            char_count += 1
        else:
            if char_count > 0:
                compressed_string += current_char + str(char_count)
            current_char = char
            char_count = 1
    if char_count > 0:
        compressed_string += current_char + str(char_count)
    return compressed_string



# Main.
string = "aaakkkkhffffhhhss"
ans = getCompressedString(string)
print(ans)
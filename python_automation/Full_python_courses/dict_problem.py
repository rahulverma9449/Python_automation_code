# string = "aaaaabbbbbcccddddfffjjjkkksss"
#
# dict_str = {}
#
# for char in string:
#     if char not in dict_str:
#         dict_str[char] = 1
#     else:
#         dict_str[char] += 1
#
# print(dict_str)


#####################

# string = "aaaaadddfffgghh"
# dict_str = {}
#
# for char in string:
#     if char not in dict_str:
#         dict_str[char] = 1
#     else:
#         dict_str[char] += 1
#
# print(dict_str)

#
# from collections import Counter
#
# def removeduplicate(input):
#     input = input.split("")
#     list = Counter(input)
#
#     s = "".join(list.keys())
#
#     print(s)
#
#
# input = "ahkjhkjddskadjhsdhjf"
# print(input)

s = " AASSSSSSDDDDDDDDjjjjjjjjjjcccccccccchdksneiuurhfhd"
l = s.split()
k = []
for i in l:
    if (s.count(i) >=1 and (i not in k)):
        k.append(i)
print(k)
###
string = 'python is great is  great power java and '
print(', '.join(set(string.split())))

####
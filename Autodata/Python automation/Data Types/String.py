# def char_frequency(str1):
#     dict = {}
#     for n in  str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('aaabbbcccdddhhhjjjsssnnyyyuue'))
#
# a = "Hello, World! "
# print(a.replace("M", "J"))

# full_name = 'Rahul verma'
# name_s = full_name.split()
# print(full_name)
# print(name_s)
#
#
# url = "hhtps://www.amazon.com/"
# is_home = url.endswith('.com/')
# print(is_home)

# url = "this%20is%20the%20python%20"
# # java = url.replace("%20", " ")
# # print(url)
# # print(java)
# my_var = "I Love {} programming language".format("Python")
# print(my_var)
# my_var1 = "{} is {} years old".format("rahul", 26)
# print(my_var1)
# my_var2 = "{name} is {age} years old".format(name="rahul", age = 27)
# print(my_var2)
# my_var3 = "{0} is {1} years old".format("rahul", 27)
# print(my_var3)


pc = ['Dell','HP','Toshiba']
print(len(pc))
pc.append('apple')
print(pc)
x = pc.pop()
print(pc)
print(x)
pc.remove("HP")
print(pc)



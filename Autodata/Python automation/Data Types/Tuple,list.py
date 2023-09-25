# # List mutable and Tuple immutable data type
# val = [1, 2, "rahul", 4.5]
# print(val[1])
#
# val[2] = "RAHUL"
# print(val)
#
# # Dictionary Data types
# dic = {"a":2 , 4:"bcd", "c": "Hello world"}
# print(dic[4])
# print(dic["c"])
#
# dict = { }
#
# dict["firstname"] = "Rahul"
# dict["lastname"] = "shetty"
#
# print(dict)

#values = [1, 2, "rahul", 4, 5]
# List is data type that allows multiple values and can be different data types
# print(values[0])
# print(values[3])
# print(values[-1])
# print(values[1:4])
# values.insert(3, "verma")
# print(values)
# values.append("End")
# print(values)

# values[2] = "RAHUL" # updating values
# del values[0]
# print(values)


# b, c, d = 5, 6.4, "Great"
# print("{} {}".format("Value is", b))
#
# print(type(b))
#
# print(type(b))
# print(type(c))
# print(type(d))
# a = "string in a double quote"
# b = 'string in a single quote'
#
# print(a)
# print(b)
#
# print(a, "concatenated with", b)
# print(a+"concated with "+b)


countries = ["USA", "Mexico", 'Canada', 'India','German', 'Japan']
print(type(countries))
no_of_countries = len(countries)
print(no_of_countries)

# Adding element to list

countries.append('China')
print(countries)
print(len(countries))

# removing element from list
countries.remove('Canada')
print(countries)

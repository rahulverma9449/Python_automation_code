# meal = {"breakfast" : "egg", "lunch": "salad"}
#
# my_breakfast = meal["breakfast"]
# print(my_breakfast)
#
# meal["dinner"] = "steak"
# print(meal)
#
#
# capitals = {"INDIA": "Delhi","haryana": "chandigarh", "AP":"hydrabad"}
# print(type(capitals))
#
# # getting items from the Dic.
#
# # france = capitals["France"]
# # print(france)
#
# france1 = capitals.get("France")
# print(france1)

##############################
# Adding items in dict.

# capitals = {"INDIA": "Delhi","haryana": "chandigarh", "AP":"hydrabad"}
# print("before add")
# print(capitals)
# capitals["Kenya"] = "nairobi"
# print("After add")
# print(capitals)
#
#
# # Option 2
#
# capitals.update({"japan":"oluu"})
# print("Add option2")
# print(capitals)
#
# d = {'a': 1, 'b': 2}
# print(d)
# print(type(d))
# d['a'] = 100
# d['b'] = 300
# d['c'] = 4
# d['d'] = 5
# print(d)
# d.setdefault('', 43)
# print(d)
# print(d.setdefault("f", 500))
# print("after using setdefault():", d)


#
# capitals = {"INDIA": "Delhi","haryana": "chandigarh", "AP":"hydrabad"}
# all_keys = capitals.keys()
# all_values = capitals.values()
# print(all_keys)
# print(all_values)
# employee = {"name": " john verma",
#             "age": 25,
#             "phone": 168757853214,
#             "title": " Sr. Software Developer",
#             "skills": ["AWS", "Python", "JAVA", "Docker"]}
# e_name = employee['name']
# e_age = employee['age']
# e_skills = employee['skills']
# print(type(e_skills))
# user_skill_count = len(e_skills)
# print(f"User has {user_skill_count} skills")
# print(" User has {} skills".format(user_skill_count))



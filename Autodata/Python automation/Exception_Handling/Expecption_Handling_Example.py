# try:
#     a = 5 / 0
# except:
#     print("Dont divide by 0")
# Example: Catch specific exception

# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print("Dont divide by 0")

# -- Example: Print the actual error
# try:
#     #a = 5 / 0
#     b = {'name': 'foo', 'age': 26}
#     x = b['school']
# # except Exception as e:
# except KeyError:
#     print(f"Key issue ")
# except ZeroDivisionError:
#     print("Dividing by zero")

# Example: raise an exception
try:
     a = 5 / 0
    # print(foo)
except Exception as e:
    print(f" Error has happened: {e}")
    raise Exception("Something is went wrong")














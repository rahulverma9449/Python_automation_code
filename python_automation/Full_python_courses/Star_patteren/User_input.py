# def pattern(name):
#     for i in range(len(name)):
#         #A
#         if name[i]=="A":
#             print_A = [[" "for i in range(6)] for j in range(7)]
#             for row in range(7):
#                 for col in range(6):
#                     if ((col==0 or col==5) and row!=0) or row==3 or (row==0 and (col!=0 and col!=5)):
#                         print_A[row][col] = "*"
#                 list2.append(print_A)
#
#         # B
#         elif name[i] == "B":
#             print_B = [[" " for i in range(6)] for j in range(7)]
#             for row in range(7):
#                 for col in range(6):
#                     if (col == 0 or col == 4 ) or ((row==0 or row==3 or row == 6) and (col>0 and col<4)):
#                         print_B[row][col] = "*"
#                         list2.append(print_B)
#         # c
#         elif name[i]=="c":
#         print_C= [[" " for i in range(6)] for j in range(7)]
#         for row in range(7):
#             for col in range(6):
#                 if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and col!=0):
#                     print_C[row][col] = "*"
#                     list2.append(print_C)

# a,b = map(int, input().split())
#
# if a == 0 and b ==0:
#     print(1)
# else:
#     result = 1
#     for i in range(a):
#         result *= b
#     print(result)
# def lastIndex(arr, x):
#     l = len(arr)
#     if l == 0:
#         return -1
#
#     smallList = arr[1:]
#     output = lastIndex(smallList, x)
#
#     if output != -1:
#         return output + 1
#     else:
#         if arr[0] == x:
#             return 0
#         else:
#             return -1
#
#
# arr = [1, 4, 3, 5, 6]
# x = 4
# lastIndex(arr, x)

# Python program to count Even and Odd numbers in a List

# list of numbers
# list1 = [4,23,1,2,3,2]
#
# even_count, odd_count = 0, 0
# num = 0
#
# # using while loop
# while (num < len(list1)):
#
#     # checking condition
#     if list1[num] % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
#     # increment num
#     num += 1
#
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

# with open('GFG.txt', 'r') as file:
#     # reading each line
#     for line in file:
#
#         # reading each word
#         for word in line.split():
#             # displaying the words
#             print(word)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
x = Person("sanjay", "rathore")
x.printname()
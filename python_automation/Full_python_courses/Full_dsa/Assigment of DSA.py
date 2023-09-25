# # def isPlindrome(string):
# #     if len(string) < 1:
# #         return True
# #     else:
# #         if string[0] == string[-1]:
# #             return isPlindrome(string[1:-1])
# #         else:
# #             return False
# #
# #
# # str1 = input("enter string:")
# #
# # if(isPlindrome(str1)==True):
# #     print("true")
# # else:
# #     print("false")
#
#
# #************************
#
# # def sum_of_digit(n):
# #     if n == 0:
# #         return n
# #     return n % 10 + sum_of_digit(n // 10)
# # n = int(input())
# # print(n, sum_of_digit(n))
#
# #************************************
# def convertStrToInt(n):
#     l = len(n)
#     if len(n) == 1:
#         return ord(n) - ord('0')
#
#     first = ord(n[0]) - ord('0')
#     smallList = convertStrToInt(n[1:])
#     return (first * (10 ** (l - 1))) + smallList
#
#
# m = int(input())
# print(convertStrToInt(m))
#
# #*********************************
# def checkAB(s):
#     if len(s) == 0:
#         return True
#     if len(s)==1:
#         if s[0]== 'a':
#             return True
#         else:
#             return False
#     if len(s)==2:
#         if s[0]=='a' and s[1]=='a':
#             return True
#         else:
#             return False
#     if len(s)>2:
#         if s[0]=='a' and s[1]=='b' and s[2]=='b':
#             smallresult = checkAB(s[3:])
#         elif s[0]=="a" and s[1]=="a":
#             smallresult = checkAB(s[1:])
#         else:
#             return False
#         return smallresult
# s = input()
# result = checkAB(s)
# if result:
#     print("true")
# else:
#     print("false")
#
# #****************************************
# #
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_student_details():
#         print(self.name, end=" ")
#         print(self.age)
#
#     @staticmethod
#     def isTeen(age):
#         return age > 16
#
#
# a = Student.isTeen(18)
# print(a)


# import collections
# stack = collections.deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)

# import queue
# stack = queue.LifoQueue()
# stack.put(10)
# stack.put(20)
# stack.put(30)
# stack.get()
# def power(x, n):
#     if (n == 0):
#         return 1
#     else:
#         return x * power(x, n - 1)
#
#
# # Main
# from sys import setrecursionlimit
#
# setrecursionlimit(11000)
# x, n = list(int(i) for i in input().strip().split(' '))
# print(power(x, n))

def printIntersection(arr1, arr2, m, n):

    i, j = 0, 0

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j])
            j += 1
            i += 1

# Driver program to test above function

# arr1 = int(input())
#
# arr2 = int(input())
#
# m = len(arr1)
#
# n = len(arr2)
#
# printIntersection(arr1, arr2, m, n)
# from sys import stdin
#
#
# def arrayEquilibriumIndex(arr, n):
#     left_sum = 0
#     right_sum = sum(arr)
#     for i in range(n):
#         right_sum -= arr[i]
#         if left_sum == right_sum:
#             return i
#         left_sum += arr[i]
#     return -1
#
#
# # Taking input using fast I/O method
# def takeInput():
#     n = int(stdin.readline().strip())
#     if n == 0:
#         return list(), 0
#
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     return arr, n
#
#
# def printList(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
#
#
# # main
# t = int(stdin.readline().strip())
#
# while t > 0:
#     arr, n = takeInput()
#     print(arrayEquilibriumIndex(arr, n))
#
#     t -= 1
#
# def pairSum(arr, n, num):
#     result = []
#     index_dict = {}
#
#     for i in range(n):
#         complement = num - arr[i]
#         if complement in index_dict:
#             result.append((complement, arr[i]))
#         index_dict[arr[i]] = i
#
#     return result

class QueueUsingArray:
    def __init__(self):
        self.__arr=[]
        self.__count= 0
    def insertRear(self,data):
        if self.__count==10:
            return -1
        self.__arr.append(data)
        self.__count+=1
        return self.__arr
    def insertFront(self,data):
        if self.__count==10:
            return -1
        self.__arr=[data]+self.__arr
        self.__count +=1
        return self.__arr
    def deleteRear(self):
        if self.__count==0:
            print(-1)
        else:
            self.__arr.pop(-1)
            self.__count-=1
            return self.__arr
    def deleteFront(self):
        if self.__count==0:
            print(-1)
        else:
            self.__arr.pop(0)
            self.__count-=1
            return self.__arr
    def getFront(self):
        if self.__count==0:
            return -1
        return self.__arr[0]
    def getRear(self):
        if self.__count==0:
            return -1
        return self.__arr[-1]
t = [int(x) for x in input().split("")]
i = 0
A = QueueUsingArray()

while t[i]!=1:
    n =t[i]
    i += 1
    if n == 1:
        k = A.insertFront(t[i])
        if k == -1:
            print(k)
        i +=1
    elif n == 2:
        k = A.insertRear(t[i])
        if k == -1:
            print(k)
        i += 1
    elif n == 3:
        A.deleteFront()
    elif n == 4:
        A.deleteRear()
    elif n == 5:
        print(A.getFront())
    elif n == 6:
        print(A.getRear())

















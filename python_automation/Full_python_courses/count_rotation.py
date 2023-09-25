# def arrayRotateCheck(arr, n):
#     def arrayRotateCheck(arr, n):
#
#         from sys import stdin
#
#         def arrayRotateCheck(arr, n):
#             # Your code goes here
#
#             low = 0
#             high = n - 1
#
#             # Loop until the pointers meet or cross over
#             while low <= high:
#                 mid = (low + high) // 2  # Calculate the middle index
#
#                 # Check if the middle element is the minimum element
#                 if arr[mid] < arr[(mid - 1) % n] and arr[mid] < arr[(mid + 1) % n]:
#                     return mid
#
#                 if arr[low] <= arr[mid]:
#
#                     if arr[mid] > arr[high]:
#                         low = mid + 1
#                     else:
#                         high = mid - 1
#                 else:
#
#                     if arr[mid] < arr[low]:
#                         high = mid - 1
#                     else:
#                         low = mid + 1
#
#             return -1
#
#         # Taking Input Using Fast I/O
#         def takeInput():
#             n = int(stdin.readline().rstrip())
#             if n == 0:
#                 return list(), 0
#
#             arr = list(map(int, stdin.readline().rstrip().split(" ")))
#             return arr, n
#
#         # main
#         t = int(stdin.readline().rstrip())
#
#         while t > 0:
#             arr, n = takeInput()
#             print(arrayRotateCheck(arr, n))
#
#             t -= 1
s="abcd"
s[0]='c'
print(s)
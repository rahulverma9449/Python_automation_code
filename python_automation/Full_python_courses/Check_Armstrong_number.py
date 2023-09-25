# lines = int(input())
# i = 1
# while(i<=lines):
#     j = lines
#     while(j>=1):
#         if j!=i:
#             print(j, end="", flush=True)
#         else:
#             print('*', end="", flush=True)
#         j = j -1
#     print()
#     i = i + 1

# lines = int(input())
# i = 1
# j = 1
# while i <= lines:
#     j = 1
#     while j<=lines:
#         if i==j:
#             print('*', end="",flush=True)
#         else:
#             print('0', end="",flush=True)
#         j = j + 1
#     j = j - 1
#     print('*', end="",flush=True)
#     while j>=1:
#         if i==j:
#             print('*', end="",flush=True)
#         else:
#             print('0', end="", flush=True)
#         j -=1
#     print()
#     i = i +1
#
n = int(input())  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("true")
else:
    print("false")

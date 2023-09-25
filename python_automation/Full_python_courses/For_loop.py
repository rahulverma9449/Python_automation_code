# print num from 1 to n
#Giving all three values to range
# n = int(input())
# for i in range(1, n+1,1):
#     print(i)

# Only one values to range and it uses it as stop and by default 0 for start and 1 for step

# n = int(input())
# for i in range(n+1):
#     print(i)
# N to 1
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)


# N = int(input())
# N1 = (N + 1) // 2
# N2 = N // 2
#
# i = 1
# while (i <= N1):
#     # top half spaces
#     j = 1
#     while (j <= i - 1):
#         print(' ', end="")
#         j += 1
#
#     # top half stars
#     k = 1
#     while (k <= i):
#         print('* ', end="")
#         k += 1
#     print()
#     i += 1
#
# y = 1
# while (y <= N2):
#     # top half spaces
#     j = 1
#     while (j <= N2 - y):
#         print(' ', end="")
#         j += 1
#
#     # top half stars
#     k = 1
#     while (k <= N2 - y + 1):
#         print('* ', end="")
#         k += 1
#     print()
#     y += 1

# n = int(input())
# flag = False
# for d in range(2, n, 1):
#     if n % d ==0:
#         flag = True
# if flag:
#     print("not prime")
# else:
#     print("Prime")

# n  = int(input())
# for i in range(1, n+1, 1):
#     for s in range(n-i):
#         print("", end="")
#     for j in range(i, 2*i, 1):
#         print(j, end="")
#     for j in range(2*i - 2, i-1,-1):
#         print(j, end="")
#     print()


# N = 6
# for i in range(1, N + 1):
#     for j in range(i - 1):
#         print(' ', end='')
#     for j in range(i, N + 1):
#         print(j, end='')
#     print('')
# for i in range(1, N):
#     for s in range(N-i-1):
#         print(' ', end='')
#     for j in range(N-i, N + 1):
#         print(j, end='')
#     print('')

# num=int(input())
# i=0
# while num>i:
#     spaces=1
#     while spaces<=i:
#         print(" ",end="")
#         spaces=spaces+1
#     j=1
#     while num-i >=j:
#         print(j+i,end="")
#         j=j+1
#     i=i+1
#     print()
# while i>1:
#     spaces=1
#     while spaces<=i-2:
#         print(" ",end="")
#         spaces=spaces+1
#     j=num
#     k=1
#     while j>=i-1:
#         print(i+k-2,end="")
#         j=j-1
#         k=k+1
#
#     i=i-1
#     print()


# N = int(input())
# firstHalf = (N + 1) // 2
# secondHalf = N // 2
# # First Half
# currRow = 1
# while currRow <= firstHalf:
#     spaces = 1
#     while spaces <= (firstHalf - currRow):
#         print(" ", end="")
#         spaces += 1
#     currCol = 1
#     while currCol <= (2 * currRow) - 1:
#         print("*", end="")
#         currCol += 1
#
#     print()
#     currRow += 1
# # Second Half
# currRow = secondHalf
# while currRow >= 1:
#     spaces = 1
#     while spaces <= (secondHalf - currRow + 1):
#         print(" ", end="")
#         spaces += 1
#     currCol = 1
#     while currCol <= (2 * currRow) - 1:
#         print("*", end="")
#         currCol += 1
#
#     print()
#     currRow -= 1

# N = int(input())
#
# for i in range(1, N + 1, 1):
#     for up in range(1, i, 1):
#         print(N - up + 1, end='')
#
#     for j in range(i, 2 * N - i + 1, 1):
#         print(N - i + 1, end='')
#
#     for lp in range(2 * N - i, 2 * N - 1, 1):
#         print(lp - N + 2, end='')
#
#     print()
#
# for i in range(N - 1, 0, -1):
#     for up in range(1, i, 1):
#         print(N - up + 1, end='')
#
#     for j in range(i, 2 * N - i + 1, 1):
#         print(N - i + 1, end='')
#
#     for lp in range(2 * N - i, 2 * N - 1, 1):
#         print(lp - N + 2, end='')
#
#     print()




# n = int(input())
# upper = int(n/2)+1
# lower = n - upper
# start_i_lower = 0
#
# for i in range(0, upper):
#   if i != 0:
#     i = i + i
#   start = n*i + 1
#   end = start + n
#
#   for j in range(start, end):
#     print(j, end =" ")
#   start_i_lower = i
#   print()
#
# start_i_lower -= 1
#
# for i in range(0, lower):
#   if(n%2 == 0):
#     start_i_lower -= 1
#
#   start = n*(start_i_lower-1) + 1
#   end = start + n
#
#   for j in range(1, n+1):
#         print(j+n, end =" ")
#
#   print()
#
#
#
#
#
#  N=int(input())
#
# for i in range(1,N**2,(2*N)):
#     for j in range(1,N+1):
#         print(i+j-1,end=" ")
#     print()
# if N%2==0:
#     p=N-1
# else:
#     p=N-2
#
#
# for i1 in range(((N*p)+1),N,-(2*N)):
#     for j1 in range(1,N+1):
#         print(i1+j1-1,end=" ")
#     print()

#
# def fact(a):
#     a_fact = 1
#     for i in range(1, a + 1):
#         a_fact = a_fact * i
#     return a_fact
# a=fact(4)
# a
# n = int(input())
# r = int(input())
# n_fact =fact(n)
# r_fact = fact(r)
# n_r_fact = fact(n - r)
# ans = n_fact//(r_fact*n_r_fact)
# print(ans)

# n = int(input())
# i =1
# while i <=n:
#     spaces = 1
#     while spaces <= n - i:
#         print('', end='')
#         spaces += 1
#     j =1
#     p = i
#     while j<= i:
#         print(p, end='')
#         j +=1
#         p -=1
#     p= 2
#     while p <= i:
#         print(p, end='')
#         p +=1
#
#     print()
#     i +=1
#
# #
# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     start_char = chr(ord('A') + i -1)
#     while j <= i:
#         charp = chr(ord(start_char) + j - 1)
#         print(charp, end = '')
#         j = j + 1
#     print()
#     i += 1
# out put
# 5
# A
# BC
# CDE
# DEFG
# EFGHI


# def printTable(start,end,step):
#     while True:
#         c = 0
#         if start <= end:
#             c = (start - 32) * 5 / 9
#             print(start, int(c))
#             start = start + step
#         else:
#             break
# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s, e, step)
# import math
#
#
# # A utility function that returns true if x is perfect square
#
#
# def isPerfectSquare(x):
#     s = int(math.sqrt(x))
#     return s * s == x
#
#
# # Returns true if n is a Fibonacci Number, else false
#
#
# def isFibonacci(n):
#     # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
#     # is a perfect square
#     return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)
#
#
# # A utility function to test above functions
# for i in range(1, 11):
#     if (isFibonacci(i) == True):
#         print(i, "is a Fibonacci Number")
#     else:
#         print(i, "is a not Fibonacci Number ")
#


# def checkMember(n):
#     if (n ==0):
#         return 0
#     elif (n== 1):
#         return 1
#     else:
#         return checkMember(n -1 ) + checkMember(n -2 )
#
#
# n = int(input())
# if (checkMember(n%2)):
#     print("true")
# else:
#     print("false")











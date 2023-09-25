# N = int(input())
# i = 1
# sum = 0
# while i <= N:
#     if i % 2 == 0:
#         sum = sum + i
#         i = i + 1
#     else:
#          i = i + 1
#     print(sum)


# WhileLoop Prime

# n = int(input())
# k = 2
#
# while k <= n:
#     d = 2
#     flag = False
#     while d < k:
#         if(k % d == 0):
#             flag = True
#         d = d +1
#     if not (flag):
#          print(k)
#     k = k + 1

# S = int(input())
# E = int(input())
# W = int(input())
#
# while(S <= E):
#     cel = (S - 32) * 5/9
#     print(S," ",int(cel))
#     S = S + W


# while (1):
#     i = int(input())
#     if(i == 1):
#         a = int(input())
#         b = int(input())
#         c = a+b
#         print(c)
#     elif(i == 2):
#         a = int(input())
#         b = int(input())
#         c = a-b
#         print(c)
#     elif(i == 3):
#         a = int(input())
#         b = int(input())
#         c = a*b
#         print(c)
#     elif(i == 4):
#         a = int(input())
#         b = int(input())
#         c = a/b
#         print(int(c))
#     elif(i == 5):
#         a = int(input())
#         b = int(input())
#         c = a%b
#         print(int(c))
#     elif(i == 6):
#         break
#     else:
#         print("Invalid Operation")


# def reverse(n):
#     rev = 0
#     while(n > 0):
#         reminder = n % 10
#         rev = (rev  * 10) + reminder
#         n = n // 10
#     return rev
# n = int(input())
# result = reverse(n)
# print(result)


# def checkPalindrome(num):
#     temp = num
#     rev = 0
#     while(num > 0):
#         reminder = num % 10
#         rev = (rev * 10) + reminder
#         num = num // 10
#     if (temp == rev):
#         return True
#     else:
#         return False
#
# num = int(input())
# isPalindrome = checkPalindrome(num)
# if(isPalindrome):
#     print('true')
# else:
#     print('false')


# N = int(input())
#
# even = 0
# odd = 0
# while(N > 0):
#     rem = N%10
#     N = N // 10
#     if (rem % 2 == 0):
#         even = even + rem
#     else:
#         odd = odd + rem
# print(even,"", odd)
#

# N = int(input())
# N1 = 0
# N2 = 1
# i = 1
# if(N == 1):
#     print(1)
# else:
#     while(i<N):
#         Nth = N1 + N2
#         N1 = N2
#         N2 = Nth
#         i += 1
#     print(Nth)
# n = int(input())
# a = 0
# b = 1
#
# c = -1
# for i in range(n):
#     c = a + b
#     a = b
#     b = c
# print(a)
# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         print("*",end="")
#         j = j + 1
#     # empty print to go to the next line
#     print()
#     i = i + 1
# n = int(input('Enter number of rows : '))
#
# i = 1
# while i <= n:
#     j = n
#     while j >= i:
#         print("*", end=" ")
#         j -= 1
#     print()
#     i += 1

# #
# n = int(input("ENter number of rows: "))
#
# k = 1
# i = 1
# while i <=n:
#     j = 1
#     while j <=i:
#         print("{:3d}".format(k), end = "")
#         j = j +1
#         k = k +1
#     print()
#     i = i + 1


# N = int(input())
# i = 1
# while i<= N:
#     j = 1
#     while j <= i:
#         print(j,end='')
#         j += 1
#     print()

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         charP = chr(ord('A') + j - 1)
#         print(charP, end='')
#         j += 1
#     print()
#     i += 1

# print kth alphabet
# k = int(input())
# # 'A' + k - 1
# x = ord('A')
# asciiTarget = x + k - 1
# targetChar = chr(asciiTarget)
# print(targetChar)
#

# n = int(input())
# i = 1
#
# while i <= n:
#     j = 1
#     start_char = chr(ord('A') + i -1 )
#     while j <= i:
#         charP = chr(ord(start_char) + j - 1)
#         print(charP , end='')
#         j += 1
#     print()
#     i += 1

# n = int(input())
# i = 1
#
# while i <= n:
#     j = 1
#     start_char = chr(ord('A') + i -1 )
#     while j <= i:
#         charP = chr(ord(start_char) + j - 1)
#         print(charP , end='')
#         j += 1
#     print()
#     i += 1






# k = int (input())
# # 'A' +k - 1
# x = ord ('A')
# assci_target = x +  k - 1
# target_char = chr(assci_target)
# print (target_char)


# n = int(input())
# i = 1
# while (i <= n):
#     j = 1
#     while( j <= n):
#         charP = chr(ord('A') + j - 1) # to get the character.
#         print(charP,end='')
#         j += 1
#     print()
#     i += 1

# n = int(input())
# i = 1
# while (i <= n):
#     j = 1
#     start_char = chr(ord('A') + i - 1)
#     while( j <= n):
#         charP = chr(ord(start_char) + j - 1) # to get the character.
#         print(charP,end='')
#         j += 1
#     print()
#     i += 1



# n = int(input())
# currRow = 1
# while currRow <= n:
#     currCol = 1
#     ch = ord('A') + currRow - 1
#     while currCol <= currRow:
#         print(chr(ch + currCol - 1), end = "")
#         currCol += 1
#     print()
#     currRow += 1

#
# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     start_char = chr(ord('A') + i - 1)
#
#     while j <= i:
#        print(start_char, end='')
#        j += 1
#     print()
#     i += 1

# N = int(input())
# i = 1
# p = 1
# while i<=N:
#     j = 1
#     while j<=i:
#         print(p, end='')
#         j = j + 1
#         p = p + 1
#     print()
#     i = i + 1
# #

# N = int(input())
# i = 1
#
# while i <= N:
#     j = 1
#
#     while j <= (N - i + 1):
#         print(j, end="")
#         j = j + 1
#
#     print()
#     i = i + 1




# n = int(input())
# i = 1
# print("1")
# while (i <= n - 1):
#     j = 1
#     print("1", end='')
#     while (j <= i - 1):
#         print("2", end='')
#         j += 1
#     print("1", end='')
#     print()
#     i += 1

# N = int(input())
# i = 1
# print("1")
# while (i <=N-1):
#     j = 1
#     print(i, end = '')
#     while (j <= i - 1):
#             print("2", end='')
#             j = j + 1
#     print(i, end = '')
#
#     print()
#     i = i + 1


# N = int(input())
# i = 1
#
# while i <= N:
#     spaces = 1
#
#     while spaces <= N - i:
#         print(' ', end="")
#         spaces = spaces + 1
#     stars = 1
#     while stars <= i:
#         print(stars, end ="")
#         stars =  stars + 1
#     print()
#     i = i + 1

# n = int(input())
# i = 2
# while (i <= n):
#     p = i - 1
#     while p >= 1:
#         print(p, end='')
#         p -= 1
#     print()
#     i += 1

# n = int(input())
# i = 1
# while (i <= n):
#     spaces = 1
#     while spaces <= (n - i):
#         print(' ', end='')
#         spaces += 1
#
#     stars = 1
#     while stars <= i:
#         print(i, end='')
#         stars += 1
#     print()
#     i += 1



# N = int(input())
# i = 1
# while i <= N:
#     spaces = 1
#     # spaces
#     while spaces <= N - i:
#         print('', end = "")
#         spaces = spaces + 1
#     p = 1
#     j = 1
#     # Increasing seq
#     while j <= i:
#         print(p, end= '')
#         j = j + 1
#         p = p + 1
#     # Decreasing Seq
#
#     p = i - 1
#     while p >= 1:
#         print(p, end='')
#         p = p - 1
#     print()
#     i = i +1

# n = int(input())
# i = 1
# while (i <= n):
#     # spaces
#     spaces = 1
#     while (spaces <= n - i):
#         print(' ', end='')
#         spaces += 1
#
#     # increasing sequence
#     j = 1
#     p = i
#     while (j <= i):
#         print(p, end='')
#         j += 1
#         p += 1

    # # decreasing sequence
    # p = 2*i - 2
    # k = 1
    # while (k <= i-1):
    #     print(p, end='')
    #     p -= 1
    #     k = k + 1
    #
    # print()
    # i += 1


# n = int(input())
# currRow = 1
# while currRow <= n:
#     spaces = 1
#     while spaces <= (n - currRow):
#         print(" ", end="")
#         spaces += 1
#
#     currCol = 1
#     valToPrint = currRow
#     while currCol <= currRow:
#         print(valToPrint, end="")
#         valToPrint += 1
#         currCol += 1
#
#     currCol = 1
#     valToPrint = 2 * currRow - 2
#     while currCol <= currRow - 1:
#         print(valToPrint, end="")
#         valToPrint -= 1
#         currCol += 1
#     print()
#     currRow += 1


# N = int(input())
# # top half
# N1 = (N + 1) // 2
#
# i = 1
# while i <= n1:
#     j = 1
#     # top spaces
#     while j <= n1 - i:
#         print(' ', end='')
#         j += 1
#
#     # top stars
#     k = 1
#     while k <= 2 * i - 1:
#         print('*', end='')
#         k += 1
#     i += 1
#     print()
#
# n2 = n // 2
# y = 1
# while y <= n2:
#
#     # bottom spaces
#     l = 1
#     while l <= y:
#         print(' ', end='')
#         l += 1
#
#     # bottom star
#     m = 1
#     while m <= n1 + n2 - 2 * y:
#         print('*', end='')
#         m += 1
#
#     y += 1
# #     print()
# N = int(input())
# N1 =N//2
# print(N1)
#
# n = int(input())
# # top half
# n1 = (n + 1) // 2
#
# i = 1
# while i <= n1:
#     j = 1
#     # top spaces
#     while j <= n1 - i:
#         print(' ', end='')
#         j += 1
#
#     # top stars
#     k = 1
#     while k <= 2 * i - 1:
#         print('*', end='')
#         k += 1
#     i += 1
#     print()
#
# n2 = n // 2
# y = 1
# while y <= n2:
#
#     # bottom spaces
#     l = 1
#     while l <= y:
#         print(' ', end='')
#         l += 1
#
#     # bottom star
#     m = 1
#     while m <= n1 + n2 - 2 * y:
#         print('*', end='')
#         m += 1
#
#     y += 1
#     print()


# n = int(input())
# firstHalf = (n + 1) // 2
# secondHalf = n // 2
#
# # First Half
# currRow = 1
# while currRow <= firstHalf:
#     spaces = 1
#     while spaces <= (firstHalf - currRow):
#         print(" ", end="")
#         spaces += 1
#
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
#
#     currCol = 1
#     while currCol <= (2 * currRow) - 1:
#         print("*", end="")
#         currCol += 1
#
#     print()
#     currRow -= 1




####

# N = int(input())
# i = 1
# while (i <= N):
#     # starting numbers
#     j = 1
#     while (j <= i):
#         print(j, end='')
#         j += 1
#
#     # spaces
#     k = 1
#     while (k <= 2 * N - 2 * i):
#         print(' ', end='')
#         k += 1
#
#     # ending spaces
#     l = 1
#     p = i
#     while (l <= i):
#         print(p, end='')
#         p -= 1
#         l += 1
#
#     print()
#     i += 1

# n = int(input())
# totalspace = n * 2 - 2
# row = 1
# while (row <= n):
#     column = 1
#     while (column <= row):
#         print(column, end='')
#         column = column + 1
#
#     space = 1
#     while (space <= totalspace):
#         print(" ", end='')
#         space = space + 1
#
#     totalspace = totalspace - 2
#
#     column = row
#     while (column > 0):
#         print(column, end='')
#         column = column - 1
#     row = row + 1
#     print()

#todo

# N = int(input())
# i=1
# j=1
# while i<=N:
#     j =1
#     while j<=N:
#         if i==j:
#             print("*", end='')
#         else:
#             print("0", end='')
#         j=j+1
#     j = j-1
#     print("*", end='')
#     while j >=1:
#         if i ==j:
#             print("*", end='')
#         else:
#             print("0", end='')
#         j=j-1
#     print("")
#     i =i+1


# N = int(input())
# for i in range(1, N + 1):
#     for s in range(0, N - i):
#         print(' ', end='')
#
#     for c in range(i, 2 * i, 1):
#         print(c, end='')
#
#     # decreaing
#     for v in range(2 * i - 2, i - 1, -1):
#         print(v, end='')
#     print()













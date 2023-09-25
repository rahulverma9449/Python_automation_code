# n = int(input())
# i = 1
# while i <=n:
#     j = i
#     while j >=1:
#         print(chr(ord('A') + n-j), end = '')
#         j = j - 1
#     print()
#     i = i + 1

#**************************************

n = int(input())
i = 1
while i <=n:
    spaces = i
    while spaces >=n-i:
        print(" ", end = '')
        spaces = spaces + 1
stars = i
while stars <= i:
    print("1", end = "")
    stars = stars - 1
print()
i = i + 1



# '''
#     In order to print two or more integers in a line separated by a single
#     space then you may consider printing it with the statement,
#
#     print(str(num1) + " " + str(num2))
#     Take Minimum value as MIN_VALUE = -2147483648
#
# '''
#
# from sys import stdin
#
#
# def findLargest(arr, nRows, mCols):
#     # Your code goes here
#     rowIndex = 0
#     colIndex = 0
#     rowSum = -2147483648
#     colSum = -2147483648
#
#     for i in range(nRows):
#         tempSum = sum(arr[i])
#         if (tempSum > rowSum):
#             rowSum = tempSum
#             rowIndex = i
# #
# #     for j in range(mCols):
# #         tempSum = 0
# #         for i in range(nRows):
# #             tempSum += arr[i][j]
# #         if (tempSum > colSum):
# #             colSum = tempSum
# #             colIndex = j
# #
# #     if (rowSum >= colSum):
# #         print("row " + str(rowIndex) + " " + str(rowSum))
# #     else:
# #         print("column " + str(colIndex) + " " + str(colSum))
# #
# #         # if nRows==0 and mCols==0:
# #     #     #print("row"+" "+str(0)+" "+str(-2147483648))
# #     #     #return
# #     # col_max = -1
# #     # col_index = -1
# #     # row_max=-1
# #     # row_index=-1
# #     # for i in range(mCols):
# #     #     col_sum = 0
# #     #     for j in range(nRows):
# #     #         col_sum+=arr[j][i]
# #     #     if col_max<col_sum:
# #     #         col_max=col_sum
# #     #         col_index = i
# #
# #     # for i in range(nRows):
# #     #     row_sum=0
# #     #     for j in range(mCols):
# #     #         row_sum+=arr[i][j]
# #     #     if row_max<row_sum:
# #     #         row_max=row_sum
# #     #         row_index=i
# #     # if col_max>row_max:
# #     #     print("column"+" "+str(col_index)+" "+str(col_max))
# #     # elif row_max>=col_max:
# #     #     print("row"+" "+str(row_index)+" "+str(row_max))
# #
# #
# # # Taking Input Using Fast I/O
# # def take2DInput():
# #     li = stdin.readline().rstrip().split(" ")
# #     nRows = int(li[0])
# #     mCols = int(li[1])
# #
# #     if nRows == 0:
# #         return list(), 0, 0
# #
# #     mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
# #     return mat, nRows, mCols
# #
# #
# # # main
# # t = int(stdin.readline().rstrip())
# #
# # while t > 0:
# #     mat, nRows, mCols = take2DInput()
# #     findLargest(mat, nRows, mCols)
# #
# #     t -= 1
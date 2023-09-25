# raw = 6
# for i in range(raw):
#     for j in range(i):
#         print(i, end ='')
#     print()
#*****************************

# raw = 5
# for i in range(1, raw+1):
#     for j in range(1, i+1):
#         print(j, end ='')
#     print('')

#************************
# raw = 5
# b = 0
# for i in range(raw, 0,-1):
#     b +=1
#     for j in range(1, i+1):
#         print(b, end ='')
#     print('')
#************************
# raw = 5
# num = raw
# for i in range(raw, 0,-1):
#
#     for j in range(0, i):
#         print(num, end ='')
#     print('\r')
#*************************
# raw = 5
# i = 1
# while i <= raw:
#     j = 1
#     while j <= i:
#         print((i * 2 - 1), end= "")
#         j = j + 1
#     i = i + 1
#     print("")
#********************
# raw = 5
#
# for i in range(raw, 0, -1):
#     num = i
#     for j in range(0,i):
#         print(num, end='')
#     print('\r')
#
#
# for i in range(raw, 0, -1):
#     num = i
#     for j in range(0,i):
#         print(num, end='')
#     print('\r')
#********************************
# start = 1
# stop = 2
# num = stop
# for row in range(2,6):
#     for col in range(start, stop):
#         num -= 1
#         print(num, end='')
#     print('')
#     start = stop
#     stop += row
#     num = stop
#**********************************
# row = 6
# for i in range(1, row):
#     num = 1
#     for j in range(row,0,-1):
#         if j >i:
#             print("", end='')
#         else:
#             print(num, end="")
#             num += 1
#     print('')
#***********************************
#
# row = 5
# k = 2 * row -2
# for i in range(row, -1, -1):
#     for j in range(k, 0,-1):
#         print(end="")
#     k = k  + 1
#     for j in range(0, i +1):
#         print("*", end="")
#     print('')
#**************************************

# size = 7
# m  = (2 * size) -2
# for i in range(0, size):
#     for j in range(0,m):
#         print(end ='')
#     m = m - 1
#     for j in range(0, i + 1):
#         print("*", end = '')
#     print('')
#***************************************
# row = 14
# print('*' * row, end='\n')
# i = (row // 2) - 1
# j = 2
# while i != 0:
#     while j <= (row - 1):
#         print("*" * i, end ='')
#         print("_" * j, end='')
#         print("*" * i, end='\n')
#         i = i - 1
#         j = j + 2
#*************************************
def spiralPrint(mat, nRows, mCols):
    top = 0
    bottom = nRows - 1
    left = 0
    right = mCols - 1
    dir = 0

    while top <= bottom and left <= right:
        if dir == 0:
            for i in range(left, right+1):
                print(arr[top][i], end=' ')
            top += 1
        elif dir == 1:
            for i in range(top, bottom+1):
                print(arr[i][right], end=' ')
            right -= 1
        elif dir == 2:
            for i in range(right, left-1, -1):
                print(arr[bottom][i], end=' ')
            bottom -= 1
        elif dir == 3:
            for i in range(bottom, top-1, -1):
                print(arr[i][left], end=' ')
            left += 1

        dir = (dir + 1) % 4


t = int(input())
for _ in range(t):
    nRows, mCols = map(int, input().split())
    arr = []
    for i in range(nRows):
        row = list(map(int, input().split()))
        arr.append(row)
    spiralPrint(mat, nRows, mCols)
    print()
# def swapAlternate(li, n) :
#     # Your code
#     l = len(li)
#     if l%2 == 0:
#         for i in range(0,l,2):
#             li[i],li[i+1] = li[i+1],li[i]
#     else:
#         for i in range(0,l-1,2):
#             li[i],li[i+1] = li[i+1],li[i]
#     for i in li:
#         print(i,end =' ')
# n = int(input())
# li = [int(x) for x in input().split()[:n]]
# rev(li)

# N = eval(input())
# if type(N)!= list:
#     print()
# else:
#     for i in range(0, len(N)-1):
#         N[i],N[i+1] =N[i+1], N[i]
#     print(N)
#
# def find_unique(li, n):
#     for i in range(n):
#         for j in range(0, n):
#             if i == j:
#                 continue
#             if (li[i] == li[j] and j == n):
#                 return li[i]
#
#
# n = int(input())
# li = [2, 3, 1, 6, 3, 6, 2]
# ele = find_unique(li, n)
# print(ele)


# def findSingle(ar, N):
#     res = ar[0]
#
#
#     for i in range(1, N):
#         res = res ^ ar[i]
#
#     return res
#
#
#
# ar = int(input())
# print(findSingle(ar, len(ar)))

#
# def find_unique(li, n):
#     for i in range(n):
#         j = 0
#         while (j < n):
#             if i != j:
#                 if li[i] == li[j]:
#                     break
#             j = j + 1
#         if j == n:
#             return li[i]


# 1
# 9
# arr = [0, 7, 2 ,5 ,4 ,7 ,1, 3, 6]
#
#
# def duplicateNumber(arr, n):
#     for i in range(n):
#         j = 0
#         while (j <= n):
#             if i != j:
#                 if arr[i] == arr[j]:
#                     break
#             j = j + 1
#         if j == n:
#             return arr[i]

# def duplicateNumber(arr, n):
#     for i in range(0, len(arr)):
#         for j in range(i +1, len(arr)):
#             if(arr[i] ==arr[j]):
#                 return arr[i]

# def findTriplet(arr, n, x):
#     set = 0
#     for i in range(0, n - 1):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if (arr[i] + arr[j] + arr[k]) == x:
#                     set = set + 1
#                     return set
#
#
#         return False



def binarySearch(arr : List[int], n : int, x : int) :
    #Your code goes here
    low = 0
    high = n -1
    for i in range(0, n):
        if low > high:
            return -1
        mid = int((high + low)/2)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid-1
        else:
            return mid

        if list[mid] == x:
            return mid

        elif list[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

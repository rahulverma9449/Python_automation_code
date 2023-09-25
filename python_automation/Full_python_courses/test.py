# def printLeaders(arr, size):
#     max_from_right = arr[size - 1]
#     print(max_from_right, end=' ')
#     for i in range(size - 2, -1, -1):
#         if max_from_right <= arr[i]:
#             strong = []
#             strong.append(i)
#             #print(arr[i], end=' ')
#             max_from_right = arr[i]
#
#
# # Driver function
# arr = int(input())
# arr = list(map(int, input().split()))
# printLeaders(arr, len(arr))

def printLeaders(arr, size):
    for i in range(0, size):
        flag = 0
        print("arr[i]", arr[i])
        for j in range(i+1, size):
            if arr[j] > arr[i]:
                flag =1
                break
        if flag ==0:
            print(arr[i], end ="")

arr = int(input())
arr = list(map(int, input().split()))
printLeaders(arr, len(arr))
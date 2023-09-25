# Read input as sepcified in the question
# Print output as specified in the question
#
# N = int(input())
# lt = []
# for i in range(0, N):
#     t = int(input())
#     lt.append(t)
#
# sm = 0
# for et in lt:
#     sm = sm + et
# print(sm)

# n = int(input())
# pr = input()
# a = pr.split()
# sum = 0
# for i in a:
#     sum = sum + int(i)
# print(sum)


# N = set()
# for i in range(int(input())):
#     N.add(input( ))
# print(len(N))
# # print(a.add('HackerRank'))
# # print(a)

# s = set()
# for i in range(int(input())):
#     s.add(input())
# print(len(s))
# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
# #     c = input().split()
# #     if c[0] == 'pop':
# #         s.pop()
# #     elif c == 'remove':
# #         s.remove(int(c[1]))
# #     else:
# #         s.discard(int(c[1]))
# # print(sum(s))
#
#
# N = int(input())
# li = [int(x) for x in input().split()]
# ele = int(input())
#
# isfound = False
# for i in range(len(li)):
#     if li[i] == ele:
#         print(i)
#         isfound = True
#         break
# if isfound is False:
#     print(-1)

# def linear_search(li,ele):
#     for i in range(len(li)):
#         if li[i] == ele:
#             return i
#         return -1
# li = [1, 2, 3, 6, 5]
# index = linear_search(li, int(input()))
# print(index)

## ReverseList program with len() function

# def reverse_l(li):
#     length = len(li)
#     for i in range(length//2):
#         li[i], li[length-i-1] = li[length-i-1],li[i]
#
# li = [1, 2, 3, 4, 5, 6]
# reverse_l(li)
# print(li)

## ReverseList program without len() function


# def reverse_l(li):
#     length = len(li)
#     for i in range(length//2):
#         li[i], li[-i-1] = li[-i-1],li[i]
#
# li = [1, 2, 3, 4, 5, 6]
# reverse_l(li)
# print(li)
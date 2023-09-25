#method-1  Using *set()
# list = [100,99,1,1,5,8,34,34,0,22,22]
# print(list)
# res = [*set(list)]
# print(res)

#method-1 Using list comprehension

# print(list)
# res = []
# [res.append(x) for x in list if x not in res]
# print(str(res))



#Method-3: Using set()
list1 = [100,99,1,1,5,8,34,34,0,22,22]
print(str(list1))
list1 = list(set(list1))
print(str(list1))

# Method 4: Using list comprehension + enumerate()

list = [100,99,1,1,5,8,34,34,0,22,22]
print(str(list))
res = [i for n, i in enumerate(list) if i not in list[:n]]
print(str(res))


# Method 5: Using collections.OrderedDict.fromkeys()
from collections import OrderedDict
list2 = [100,99,1,1,5,8,34,34,0,22,22]
print(str(list2))
res = list(OrderedDict.fromkeys(list2))
print(str(res))

#Method 6: Using in, not in operators

# list1 = [100,99,1,1,5,8,34,34,0,22,22]
# print(str(list1))
# res = []
# for i in list1:
#     if i not in res:
#         res.append(i)
# print(str(res))


# Method 7: Using list comprehension and Array.index() method.
#
# list_arr = [100,99,1,1,5,8,34,34,0,22,22]
# print(str(list_arr))
#
# res = [list_arr[i] for i in range(len(list_arr)) if i == list_arr.index(list_arr[i])]
#
# print(res)

#Method 8: Using Counter() method.

# from collections import Counter
# list_arr = [100,99,1,1,5,8,34,34,0,22,22]
# print(str(list_arr))
#
# temp = Counter(list_arr)
# res = [*temp]
# print(res)

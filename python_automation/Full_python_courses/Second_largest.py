def secondHighestElement(arr, n):
    unique_elements = set(arr)
    # taking care of some base cases before initiating
    if n <= 1:
        return -2147483648
    # same here
    elif len(unique_elements) == 1:
        return -2147483648
    # if the length of an array is greater than 1
    else:
        list_element = list(unique_elements)
        # we simply sort that array with sort() function
        list_element.sort()
        # because after sorting the second largest will be present at [-2] index
        # we return that index [-2]
        return list_element[-2]


t = int(input())
for index in range(t):
    n = int(input())
    if n:
        arr = [int(x) for x in input().split()]
        result = secondHighestElement(arr, n)
        print(result)
    else:
        arr = []
        result = secondHighestElement(arr, n)
        print(result)

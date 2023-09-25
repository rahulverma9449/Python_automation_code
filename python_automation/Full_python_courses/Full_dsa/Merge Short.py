def merge(a1, a2, a):
    i = 0  # current index in a1
    j = 0  # current index in a2
    k = 0  # current index in a (output array)

    # merge elements from a1 and a2 into a
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            j += 1
            k += 1

    # add any remaining elements from a1 or a2
    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1

    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1


def mergesort(a):
    if len(a) == 1 or len(a) == 0:
        return
        # split the array in half
    mid = len(a) // 2
    a1 = a[mid:]
    a2 = a[:mid]

    # recursively sort the left and right halves
    mergesort(a1)
    mergesort(a2)

    # merge the sorted halves
    merge(a1, a2, a)


# Main
n = int(input())
a = list(int(i) for i in input().strip().split(' '))
mergesort(a)
print(*a)

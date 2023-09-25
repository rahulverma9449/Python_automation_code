from sys import stdin

def insertionSort(arr, n) :

    #Your code goes here

    for i in range(1,len(arr)):
        n = arr[i]
        j = i -1
        while j >= 0 and n < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = n
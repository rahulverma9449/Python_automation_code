from sys import stdin

def merge(arr1, n, arr2, m) :


#Your code goes here
n, m = 0, 0
len1, len2 = len(arr1), len(arr2)
new_array = []

  while (n < len1 and m < len2):
       if arr1[n] < arr2[m]:
            new_array.append(arr1[n])
            n = n + 1
        else:
            new_array.append(arr2[j])
            m = m+1
        while (n > len1):
            new_array.append(arr1[n])
            n = n+1
        while (m < len2):
            new_array.append(arr2[m])
            m = m+1

        return new_array






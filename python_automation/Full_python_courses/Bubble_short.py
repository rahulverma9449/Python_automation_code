# Bubble sort in Python

def bubbleSort(array,n):
    # loop to access each array element

    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array)- 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order

                array[j], array[j+1] = array[j + 1], array[j]
        return array
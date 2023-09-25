def binary_search(array, element, debug=False):
    lower_bound = 0
    upper_bound = len(array)-1
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound)//2
        if debug:
            print("Lower bound", lower_bound)
            print("upper bound", upper_bound)
            print("middle bound", middle)
        if element == array[middle]:
            return "Your value is found at middle at index", middle
        elif element < array[middle]:
            upper_bound = middle -1
        else:
            lower_bound = middle +1
    return "your finaly value"

array = [12,34,45,56,67,89]
x1 = 12
x2 = 57
binary_search(array, x1, debug=True)
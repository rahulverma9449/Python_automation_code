# class Node:
#     def __init__(self, initData):
#         self.data = initData
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.__head = None
#         self.__count = 0
#
#     def push(self, element):
#         newNode = Node(element)
#         newNode.next = self.__head
#         self.__head = newNode
#         self.__count = self.__count + 1
#
#     def pop(self):
#         if self.isEmpty() is True:
#             print("Hey!Stack is Empty!")
#             return
#         data = self.__head.data
#         self.__head = self.__head.next
#         self.__count = self.__count - 1
#         return data
#
#     def top(self):
#         if self.isEmpty() is True:
#             print("Hey! Stack is Empty!")
#             return
#         data = self.__head.data
#         return data
#
#     def size(self):
#         return self.__count
#
#     def isEmpty(self):
#         return self.size() == 0
# s=Stack()
# s.push(12)
# s.push(13)
# s.push(15)
# while s.isEmpty() is False:
#     print(s.pop())
# s.top()
def calculateSpan(price, S):
    n = len(price)
    # Create a stack and push index of first element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    S[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):

        # Pop elements from stack while stack is not
        # empty and top of stack is smaller than price[i]
        while (len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i] is
        # greater than elements after top of stack
        S[i] = i + 1 if len(st) == 0 else (i - st[-1])

        # Push this element to stack
        st.append(i)


# A utility function to print elements of array
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")


# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price) + 1)]

# Fill the span values in array S[]
calculateSpan(price, S)

# Print the calculated span values
printArray(S, len(price))
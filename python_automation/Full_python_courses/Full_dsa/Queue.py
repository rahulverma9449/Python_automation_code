# class QueueUsingArray:
#
#     def __init__(self):
#         self.__arr = []
#         self.__count = 0
#         self.__front = 0
#
#     def enqueue(self, data):
#         self.__arr.append(data)
#         self.__count +=1
#
#     def dequeue(self):
#         if self.__count == 0:
#             return -1
#         element = self.__arr[self.__front]
#         self.__front += 1
#         self.__count -= 1
#         return element
#
#     def front(self):
#         if self.__count == 0:
#             return -1
#         return self.__arr[self.__front]
#
#     def size(self):
#         return self.__count
#
#     def isEmpty(self):
#         return self.size() == 0
#
#
# q =QueueUsingArray()
# q.enqueue(23)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# while(q.isEmpty() is False):
#     print(q.front())
#     q.dequeue()
#
# print(q.dequeue())

from sys import stdin


# Following is the structure of the node class for a Singly Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Define data members and __init__()

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.__size
        # Implement the getSize() function

    def isEmpty(self):
        return self.__size == 0
        # Implement the isEmpty() function

    def enqueue(self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next
        self.__size += 1
        # Implement the enqueue(element) function

    def dequeue(self):
        if self.__head is None:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return data
        # Implement the dequeue() function

    def front(self):
        if self.__head is None:
            return -1
        return self.__head.data
        # Implement the front() function


# main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2:
        print(queue.dequeue())

    elif choice == 3:
        print(queue.front())

    elif choice == 4:
        print(queue.getSize())

    else:
        if queue.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
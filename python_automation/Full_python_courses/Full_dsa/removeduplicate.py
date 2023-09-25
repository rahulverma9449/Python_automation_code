from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicates(head):
    # Your code goes here
    # If the list is empty or has only one element, there are no duplicates
    if head is None or head.next is None:
        return head

    # Create a hash set to keep track of seen values
    seen = set()

    # Initialize current and previous pointers
    current = head
    previous = None

    # Traverse the list
    while current is not None:
        # If the current node's value is already in the set, remove it from the list
        if current.data in seen:
            previous.next = current.next
        else:
            # Otherwise, add the value to the set and move the previous pointer forward
            seen.add(current.data)
            previous = current

        # Move the current pointer forward
        current = current.next

    return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1
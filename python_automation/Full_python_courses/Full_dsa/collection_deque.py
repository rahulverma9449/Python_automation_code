# import collections
# stack = collections.deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)

# stack = collections.deque()
# not stack
# import queue
# stack = queue.LifoQueue()
# stack = queue.LifoQueue(3)
# stack.put(10)
# stack.put(20)
# stack.put(30, timeout=1)
# print(stack.get())
# print(stack.get())
# print(stack.get())
queue = []
def enqueue():
    element = input("Enter the element:")
    queue.append(element)
    print(element, "is added to queue!")
def dequeue():
    if not queue:
        print("queue  is empty!")
    else:
        e = queue.pop(0)
        print("removed element: ", e)

def display():
    print(queue)

while True:
    print("Select the operation 1.add 2.remove 3.show 4.quit")
    choice = int(input())
    if choice ==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct operation!")

import queue
#
# # s = [1, 2, 3]
# # s.append(4)
# # s.append(5)
# #
# # print(s.pop())
# # print(s.pop())
#
# # q = queue.Queue()
# # q.put(1)
# # q.put(2)
# # q.put(3)
# # q.put(4)
# # q.put(5)
# #
# # while not q.empty():
# #     print(q.get())
#
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
#
# while not q.empty():
#     print(q.get())
#
# class QueueUsingTwoStacks:
#
#     def __init__(self):
#         self.__s1 = []
#         self.__s2 = []
#
#     def enqueue(self, data):
#         while(len(self.__s1) !=0):
#             self.__s2.append(self.__s1.pop())
#         self.__s1.append(data)
#         while(len(self.__s2) !=0):
#             self.__s1.append(self.__s2.pop())
#         return
#         # O(n)
#     def dequeue(self):
#         if len(self.__s1) == 0:
#             return -1
#         return self.__s1.pop()
#     def front(self):
#         if len(self.__s1) == 0:
#             return -1
#         return self.__s1[-1]
#
#     def size(self):
#         return len(self.__s1)
#
#
#     def isEmpty(self):
#         return self.size() == 0
#
#
#
# q = QueueUsingTwoStacks()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
#
# while(q.isEmpty() is False):
#     print(q.front())
#     q.dequeue()
# from queue import Queue
#
# def reverseQueueFirstKElements(k, Queue):
#   if (Queue.empty() == True or
#       k > Queue.qsize()):
#     return
#   if (k <= 0):
#     return
#
#   Stack = []
#
#   for i in range(k):
#     Stack.append(Queue.queue[0])
#     Queue.get()
#
#   while (len(Stack) != 0 ):
#     Queue.put(Stack[-1])
#     Stack.pop()
#
#   for i in range(Queue.qsize() - k):
#     Queue.put(Queue.queue[0])
#     Queue.get()
#
# def Print(Queue):
#   while (not Queue.empty()):
#     print(Queue.queue[0], end =" ")
#     Queue.get()
#
# if __name__ == '__main__':
#   Queue = Queue()
#   Queue.put(5)
#   Queue.put(10)
#   Queue.put(15)
#   Queue.put(20)
#   Queue.put(25)
#
#   k = 5
#   reverseQueueFirstKElements(k, Queue)
#   Print(Queue)

from sys import stdin
import queue

def reverseKElements(inputQueue, k):
    if(inputQueue.empty()) or (k > inputQueue.qsize())
        return inputQueue
    if k <= 0:
        return inputQueue
    stack = list()
    for i in range(k):
        stack.append(inputQueue.get())

    while not isEmpty(stack):
        inputQueue.put((stack.pop()))

    for i in range(inputQueue.qsize() - k):
        inputQueue.put(inputQueue.get())

    return inputQueue


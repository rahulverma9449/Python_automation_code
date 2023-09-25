class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data) + "->",end= "")
        head = head.next
    print("None")
    return

def takeinput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currdata in inputList:
        if currdata == -1:
            break

        newNode = Node(currdata)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
            # curr = head
            # while curr.next is not None:
            #     curr = curr.next
            # curr.next = newNode


    return head
head = takeinput()
printLL(head)

# class solution:
#     def findMediansortedarrays(self, m, n, num1: list[int], num2: list[int]) -> float:
#         def findKth(i, j,k):
#             if i >= m:
#                 return num2[j + k -1]
#             if j >= n:
#                 return num1[i + k -1]
#             if k == 1:
#                 return min(num1[i], num2[j])
#             seen = k//2
#             mid1 = num1[i + seen -1] if i + seen - 1< m else float('inf')
#             mid2 = num2[j + seen -1] if j + seen - 1< n else float('inf')
#             if mid1 < mid2:
#                 return findKth(i + seen, j, k- seen)
#             return findKth(i, j + seen, k-seen)
#         m,n = len(num1), len(num2)
#         left, right =(m+n+1) //2, (m + n + 2) // 2
#         return (findKth(0, 0, left)+ findKth(0, 0, right)) / 2

def isPalindrome(head):
    if head is None or head.next is None:
        return True
    start = head
    end = head
    while end.next is not None and end.next.next is not None:
        start = start.next
        end = end.next.next
    prev = None
    curr = start.next
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    secondhalf = prev
    while secondhalf is not None:
        if head.data != secondhalf.data:
            return False
        head = head.next
        secondhalf = secondhalf.next

    return True




















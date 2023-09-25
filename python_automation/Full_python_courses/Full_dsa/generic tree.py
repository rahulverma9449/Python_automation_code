from sys import stdin,setrecursionlimit

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
def replacewithDepthHelper(root, depth):
    root.data = depth
    for child in root.children:
        replacewithDepthHelper(child, depth+1)
def replacewithDepth(tree):
    if not tree:
        return
    replacewithDepthHelper(tree, 0)
def createtree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root
def printlevel(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end ='')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createtree(arr)
replacewithDepth(tree)
printlevel(tree)
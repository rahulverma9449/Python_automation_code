from sys import stdin


# def spiralPrint(mat, nRows, mCols):


def spiralPrint(mat, nRows, mCols):
    # Your code goes here
    m = mCols
    n = nRows
    tempM = mCols
    tempN = nRows
    arr = []
    while tempM > int(mCols / 2) and tempN > int(nRows / 2):
        i = m - tempM
        for j in range(m - tempM, tempM):
            arr.append(str(mat[i][j]))
        j = tempM - 1
        for i in range(n - tempN + 1, tempN):
            arr.append(str(mat[i][j]))
        i = tempN - 1
        for j in range(tempM - 2, m - tempM - 1, -1):
            arr.append(str(mat[i][j]))
        j = n - tempN
        if (m != 1):
            for i in range(tempN - 2, n - tempN, -1):
                arr.append(str(mat[i][j]))
        tempN = tempN - 1
        tempM = tempM - 1
    print(" ".join(arr))


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
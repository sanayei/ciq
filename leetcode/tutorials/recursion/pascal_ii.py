
def getRow(rowIndex):

    def _pascal(i, j):
        if j == 0 or i == j:
            return 1
        return previous[j - 1] + previous[j]

    previous = []
    for i in range(0, rowIndex+1):
        current = []
        for j in range(i+1):
            current.append(_pascal(i, j))
        previous = current
    return current




if __name__ == '__main__':
    print(getRow(3))
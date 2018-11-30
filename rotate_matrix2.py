def rotate_matrix(m):
    res = [[0 for c in range(len(m))] for r in range(len(m))]
    for row in range(len(m)):
        for col in range(len(m)):
            temp = len(m)-1-row
            res[col][temp] = m[row][col]
    return res

def rotate_matrix2(m):
    top, left, bot, right = 0, 0, len(m)-1, len(m)-1
    sz = bot - top # do this because we rotate "rings" at a time
    while top < bot and left < right:
        for times in range(sz): # rotate n-1 times for an nxn "ring"
            temp = m[top][left]
            # left edge
            for i in range(sz):
                m[top+i][left] = m[top+i+1][left]
            # bottom edge
            for i in range(sz):
                m[bot][left+i] = m[bot][left+i+1]
            # right edge
            for i in range(sz):
                m[bot-i][right] = m[bot-i-1][right]
            # upper edge
            for i in range(sz):
                if right-i-1 == left:
                    m[top][right-i] = temp
                else:
                    m[top][right-i] = m[top][right-i-1]
        top += 1
        left += 1
        bot -= 1
        right -= 1
        sz = bot - top # adjust size for new "ring"
    return m


def main():
    m = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
    assert rotate_matrix(m)==rotate_matrix2(m)
    m = [['A', 'B'], ['C', 'D']]
    assert rotate_matrix(m)==rotate_matrix2(m)
    m = [['A', 'B', 'C', 'D'],
         ['E', 'F', 'G', 'H'],
         ['I', 'J', 'K', 'L'],
         ['M', 'N', 'O', 'P']]
    assert rotate_matrix(m)==rotate_matrix2(m)
    m = [['1', '2', '3', '4', '5'],
         ['6', '7', '8', '9', '10'],
         ['11', '12', '13', '14', '15'],
         ['16', '17', '18', '19', '20'],
         ['21', '22', '23', '24', '25']]
    assert rotate_matrix(m)==rotate_matrix2(m)

if __name__ == "__main__":
    main()


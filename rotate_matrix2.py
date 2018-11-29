def rotate_matrix(m):
    res = [[0 for c in range(len(m))] for r in range(len(m))]
    for row in range(len(m)):
        for col in range(len(m)):
            temp = len(m)-1-row
            res[col][temp] = m[row][col]
    return res

def rotate_matrix2(m):
    for i in range(len(m)-1):
        rotate_matrix_helper(m)
    return m

def rotate_matrix_helper(m):
    top, left, bot, right = 0, 0, len(m)-1, len(m)-1
    while top < bot and left < right:
        temp = m[top][left]
        # left edge
        for i in range(len(m)-1):
            m[top+i][left] = m[top+i+1][left]
        # bottom edge
        for i in range(len(m)-1):
            m[bot][left+i] = m[bot][left+i+1]
        # right edge
        for i in range(len(m)-1):
            m[bot-i][right] = m[bot-i-1][right]
        # upper edge
        for i in range(len(m)-1):
            if i < len(m) - 2:
                m[top][right-i] = m[top][right-i-1]
            else:
                m[top][right-i] = temp
        top += 1
        left += 1
        bot -= 1
        right -= 1


def main():
    m = [['A', 'B', 'C'],
         ['D', 'E', 'F'],
         ['G', 'H', 'I']]
    assert rotate_matrix(m)==rotate_matrix2(m)
    m = [['A', 'B'],
         ['C', 'D']]
    assert rotate_matrix(m)==rotate_matrix2(m)

if __name__ == "__main__":
    main()


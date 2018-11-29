import copy

def rotate_matrix(matrix):
    n = len(matrix)
    out_matrix = [[None for x in range(n)] for y in range(n)]
    for x in range(n):
        for y in range(n):
            out_matrix[y][n-x-1] = matrix[x][y]
    return out_matrix

def rotate_matrix_inplace(matrix):
    min_ = 0
    max_ = len(matrix)
    copy_order = ["T", "L", "B", "R"]
    while min_ < max_:
        temp = None
        for order in copy_order:
            temp = copy.deepcopy(matrix[min_])
            for y in range(max_-1, min_-1, -1):
                if order == "T":
                    matrix[min_][y] = matrix[max_-y-1][min_]
                elif order == "L":
                    matrix[max_-y-1][min_] = matrix[max_-1][max_-y-1]
                #elif order == "B":
                #    matrix[max_-1][max_-y-1] = matrix[max_-y-1][max_-1]
                #else:
                #    matrix[max_-y-1][max_-1] = temp[min_][y]
        min_ += 1
        max_ -= 1


def main():
    m = [['A', 'B', 'C'],
         ['D', 'E', 'F'],
         ['G', 'H', 'I']]
    assert rotate_matrix(m)==rotate_matrix_inplace(m)
    m = [['A', 'B'],
         ['C', 'D']]
    assert rotate_matrix(m)==rotate_matrix_inplace(m)

if __name__ == "__main__":
    main()


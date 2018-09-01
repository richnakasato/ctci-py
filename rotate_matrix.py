def rotate_matrix(matrix):
    n = len(matrix)
    out_matrix = [[None for x in range(n)] for y in range(n)]
    for x in range(n):
        for y in range(n):
            out_matrix[y][n-x-1] = matrix[x][y]
    return out_matrix

def rotate_matrix_inplace(matrix):
    raise Exception('not implemented!')


def main():
    matrix = [[None for x in range(3)] for y in range (3)]
    for x in range(3):
        for y in range(3):
            matrix[x][y] = (x, y)
    print(matrix)
    print(rotate_matrix(matrix))
    print(rotate_matrix_inplace(matrix))

if __name__ == "__main__":
    main()


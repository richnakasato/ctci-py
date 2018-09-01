import random

# cannot do in place because this will make all elements zero eventually
# so this does not work!
def zero_matrx_bf(matrix):
    width = len(matrix)
    height = len(matrix[0])
    for row in range(width):
        for col in range(height):
            if matrix[row][col] == 0:
                for x in range(width):
                    print(x, col)
                    matrix[x][col] = 0
                for y in range(height):
                    print(row, y)
                    matrix[row][y] = 0

def zero_matrx_set(matrix):
    width = len(matrix)
    height = len(matrix[0])
    rows = set()
    cols = set()
    for row in range(width):
        for col in range(height):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)
    for row in rows:
        for y in range(height):
            matrix[row][y] = 0
    for col in cols:
        for x in range(width):
            matrix[x][col] = 0

def main():
    m = 5
    n = 4
    matrix = [[random.randint(0, 9) for y in range(n)] for x in range(m)]
    for row in matrix:
        print(row)
    print()
    #zero_matrx_bf(matrix)
    #for row in matrix:
    #    print(row)
    zero_matrx_set(matrix)
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()


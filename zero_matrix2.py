class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zeroed = [[0 for c in range(len(matrix[0]))] for r in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == zeroed[r][c]:
                    for m in range(len(matrix)):
                        if matrix[m][c] != 0 and zeroed[m][c] == 0:
                            matrix[m][c] = 0
                            zeroed[m][c] = 1
                    for n in range(len(matrix[0])):
                        if matrix[r][n] != 0 and zeroed[r][n] == 0:
                            matrix[r][n] = 0
                            zeroed[r][n] = 1


def main():
    pass

if __name__ == "__main__":
    main()


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumatrix = [[0] * (cols + 1) for r in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumatrix[r][c + 1]
                self.sumatrix[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        br = self.sumatrix[row2][col2]
        above = self.sumatrix[row1 - 1][col2]
        left = self.sumatrix[row2][col1 - 1]
        tl = self.sumatrix[row1 - 1][col1 - 1]   

        return br - above - left + tl
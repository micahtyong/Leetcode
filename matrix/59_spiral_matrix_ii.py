class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for col in range(n)] for row in range(n)]
        current, maximum = 1, n * n
        def checkMax(): return current > maximum
        row, col = 0, 0
        row_end, col_end = n, n

        def goRight():
            nonlocal current, row, col, row_end, col_end
            if checkMax():
                return
            for c in range(col, col_end):
                result[row][c] = current
                current += 1
            row += 1
            goDown()

        def goDown():
            nonlocal current, row, col, row_end, col_end
            if checkMax():
                return
            for r in range(row, row_end):
                result[r][col_end - 1] = current
                current += 1
            col_end -= 1
            goLeft()

        def goLeft():
            nonlocal current, row, col, row_end, col_end
            if checkMax():
                return
            for c in range(col_end - 1, col - 1, -1):
                result[row_end - 1][c] = current
                current += 1
            row_end -= 1
            goUp()

        def goUp():
            nonlocal current, row, col, row_end, col_end
            if checkMax():
                return
            for r in range(row_end - 1, row - 1, -1):
                result[r][col] = current
                current += 1
            col += 1
            goRight()

        goRight()
        return result

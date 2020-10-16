# Source: https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # spiral matrix: right (dx=1, dy=0) -> down (dx=0, dy=-1) -> left (dx=-1, dy=0) -> up (dx=0, dy=1) -> right ...
        # m x n matrix
        # output: all the elements in the spiral order
        res = []

        def goRight():
            if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
                return
            res.extend(matrix.pop(0))
            goDown()

        def goDown():
            if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
                return
            rightMostCol = [row.pop() for row in matrix]
            res.extend(rightMostCol)
            goLeft()

        def goLeft():
            if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
                return
            res.extend(reversed(matrix.pop()))
            goUp()

        def goUp():
            if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
                return
            leftMostCol = []
            for row in matrix:
                leftMostCol = [row.pop(0)] + leftMostCol
            res.extend(leftMostCol)
            goRight()
        goRight()
        return res


# Alt
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        def checkEmpty(): return len(matrix) == 0 or len(matrix[0]) == 0

        def goLeft():
            if checkEmpty():
                return
            order.extend(matrix.pop(0))
            goDown()

        def goDown():
            if checkEmpty():
                return
            order.extend([row.pop(-1) for row in matrix])
            goRight()

        def goRight():
            if checkEmpty():
                return
            order.extend(reversed(matrix.pop(-1)))
            goUp()

        def goUp():
            if checkEmpty():
                return
            order.extend(reversed([row.pop(0) for row in matrix]))
            goLeft()

        goLeft()
        return order

# Source: https://leetcode.com/problems/spiral-matrix-ii/
# Variant: generate spiral matrix


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

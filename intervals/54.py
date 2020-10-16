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


# 0 1 2

# 1 2 3
# 4 5 6
# 7 8 9

# 1 2 3 6 9 8 7 4 5

# 1 2 3 ->

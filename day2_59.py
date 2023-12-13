# 59
# https://leetcode.com/problems/spiral-matrix-ii/description/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        val = 1

        while left <= right:    # left could be the same as right when n is an odd
            # fill every val in top row
            for c in range(left, right + 1): # right is included, right+1 is excluded
                mat[top][c] = val
                val += 1
            top += 1    # top row are filled and move down

            # fill every val in right col
            for r in range(top, bottom + 1):
                mat[r][right] = val
                val += 1
            right -= 1  # move closer to left

            # fill every val in bottom row (reverse order)
            for c in range(right, left - 1, -1): # also left should be included
                mat[bottom][c] = val
                val += 1
            bottom -= 1     # move up 1

            # fill every val in left col (reverse order)
            for r in range(bottom, top - 1, -1):
                mat[r][left] = val
                val += 1
            left += 1
        return mat
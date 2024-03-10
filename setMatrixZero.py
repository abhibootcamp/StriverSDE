'''Arrays: Day1 - Problem 1 (Leetcode Solution)
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        x = -1 * (2^31) -1
        col0 = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = x
                    if j == 0:
                        col0 = 1
                    else:
                        matrix[0][j] = x
        for i in range(n):
            if matrix[i][0] == x:
                for j in range(1, m):
                    if matrix[i][j] == x:
                        continue
                    else:
                        matrix[i][j] = 0
                matrix[i][0] = 0
        for j in range(1, m):
            if matrix[0][j] == x:
                for i in range(n):
                    matrix[i][j] = 0
        if col0:
            for i in range(n):
                matrix[i][0] = 0
        

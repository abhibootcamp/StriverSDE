''' Day1 Array : Pascal's triangle (Leetcode)
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''
def generate_row(n):
    res = []
    res.append(1)
    num = n-1
    den = 1
    for i in range(1,n):
        res.append(int(num/den))
        num *= (n-i-1)
        den *= (i+1)
    return res

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append(generate_row(i+1))
        return res

'''
Source: Leetcode
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
'''
from typing import List

class Solution:
    # O(N^2) space | O(N^2) time
    def generateMatrix(self, n: int) -> List[List[int]]:
        side_size = n
        top_x, top_y = 0,0
        matrix = []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        counter = 1
        end_value =  n**2 + 1 # 10
        # square loop
        while counter != end_value:
            if side_size == 1:
                matrix[top_x][top_y] = counter
                return matrix
            for x in range(top_x, top_x + side_size - 1): # (1)(1)
                matrix[top_y][x] = counter	# 
                counter += 1
            for y in range(top_y, top_y + side_size - 1): # (2)(0..2)
                matrix[y][top_x + side_size - 1] = counter
                counter += 1
            for x in range(top_x + side_size - 1, top_x, -1):
                matrix[top_y + side_size - 1][x] = counter
                counter += 1
            for y in range(top_y + side_size - 1, top_y, -1):
                matrix[y][top_x] = counter
                counter += 1
            top_x += 1
            top_y += 1
            side_size -= 2
        return matrix
'''
Source: leetcode.com
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        maxSteps = 0

        for i in range(len(nums) - 1): # i = [0..4]
            if nums[i] + i >= len(nums) - 1:
                return True

            maxSteps = max(nums[i],maxSteps-1) # 2

            if maxSteps == 0:
                return False
        return True

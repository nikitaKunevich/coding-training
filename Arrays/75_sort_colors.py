class Solution:
    # O(n) time | O(1) space
    # user pointers to track last non-zero item, first non-two item, current item
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur, left = 0,0 # 1, 0
        right = len(nums) - 1 # 4

        while cur <= right:        
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1
            else: cur += 1
        return nums

    # O(N) time | O(1) space
    # Use counting sort
    def sortColorsCountingSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count sort
        amounts = [0,0,0]
        for n in nums:
            amounts[n] += 1
        cur = 0
        for i in range(len(nums)):
            while amounts[cur] == 0:
                cur +=1
                if cur > 2:
                    return [nums]
            nums[i] = cur
            amounts[cur] -= 1
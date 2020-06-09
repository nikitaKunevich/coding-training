# O(n) time | O(n) space
class SolutionWSortedArray:
    def maximumProduct(self, nums: List[int]) -> int:
        s = sorted(nums)
        return max(s[0] * s[1] * s[-1], s[-3] * s[-2] * s[-1])

# O(N) time | O(1) space
class Solution:
    def maximumProduct(self, array: List[int]) -> int:
        firstMin, secondMin, firstMax, secondMax, thirdMax = float('inf'), float('inf'), float('-inf'), float('-inf'), float('-inf')
        for i in range(len(array)):
            if array[i] > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = array[i]
            elif array[i] > secondMax and array[i] <=firstMax:
                thirdMax = secondMax
                secondMax = array[i]
            elif array[i] > thirdMax and array[i] <= secondMax:
                thirdMax = array[i]
            if array[i] < firstMin:
                secondMin = firstMin
                firstMin = array[i]
            elif array[i] < secondMin and array[i] >= firstMin:
                secondMin = array[i]
        return max(firstMin * secondMin * firstMax, firstMax * secondMax * thirdMax)
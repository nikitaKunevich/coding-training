# -5, -1, 0, 5, 6
#-8, -6, 1, 2, 3, 5, 6, 12
# [1,2,3]
'''
Source: algoexpert
Write a functions that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in the ascending order with the respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input:
array=[12,3,1,2,-6,5,-8,6]
targetSum=0

Sample output:
[[-8,2,6], [-8,3,5], [-6,1,5]]
'''

# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort() # O(n*log(n))
    answer = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        subTarget = targetSum - array[i] # 8
        while right > left:
            twoSum = array[left] + array[right]
            if twoSum < subTarget: # 6 < 8
                left += 1
            elif twoSum > subTarget:
                right -= 1
            else:
                answer.append([array[i],array[left], array[right]])
                left += 1
                right -= 1
    return answer
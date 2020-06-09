# O(2^n) time | O(n) space
def maxSubsetSumNoAdjacentOne(array):
    return max(subSumOne(array, 0), subSumOne(array,1))
    
def subSumOne(array, idx):
    if idx > len(array) - 1:
        return 0
    elif idx > len(array) - 3:
        return array[idx]
    return array[idx] + max(subSumOne(array, idx + 2), subSumOne(array,idx + 3))

################################################################################
# O(n) time | O(n) space
def maxSubsetSumNoAdjacentTwo(array):
    cache = {}
    return max(subSumTwo(array, 0, cache), subSumTwo(array,1, cache))

def subSumTwo(array, idx, cache):
    if idx > len(array) - 1:
        return 0
    elif idx > len(array) - 3:
        return array[idx]
    result = cache.get(idx)
    if not result:
        cache[idx] = array[idx] + max(subSumTwo(array, idx + 2, cache), subSumTwo(array,idx + 3, cache))
    return cache[idx]
################################################################################

# O(n) time | O(1) space
def maxSubsetSumNoAdjacentThree(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    first, second = array[0], max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first + array[i], second)
        first = second
        second = current
    return second
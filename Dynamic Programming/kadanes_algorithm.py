# O(n) time | O(1) space
def kadanesAlgorithm(array):
    if len(array) == 1:
        return array[0]
    maxSum = prev = array[0]
    for i in range(1, len(array)):
        current = max(array[i], array[i] + prev)
        if current > maxSum:
            maxSum = current
        prev = current

    return maxSum
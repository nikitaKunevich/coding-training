# O(log2(n)) time | O(1) space
#iteratively

def binarySearchIterative(array, target):
    if len(array) == 0:
        return -1
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (end + start) // 2
        if target > array[mid]:
            start  = mid + 1
        elif target < array[mid]:
            end = mid - 1
        else: 
            return mid
    return -1

##############################

# O(log2(n)) time | O(log2(n)) space
# recursive
def binarySearchRecursive(array, target):
    return findSorted(array, 0, len(array) - 1, target)
    
def findSorted(array, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] > target:
        return findSorted(array, start, mid - 1, target)
    elif array[mid] < target:
        return findSorted(array, mid + 1, end, target)
    else:
        return mid
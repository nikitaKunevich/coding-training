# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    min,mid,max = float('-inf'), float('-inf'), float('-inf')
    for el in array:
        if el > min:
            if el > max:	
                min = mid
                mid = max
                max = el
            elif el > mid:
                min = mid
                mid = el
            else:
                min = el
    return [min,mid,max]
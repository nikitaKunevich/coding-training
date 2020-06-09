'''
>>> productSum([[[1]]]) #2*3*1
6
>>> productSum([2,5,[2,5,[2,5]]]) # 2 + 5 + 2 * (2 + 5 + 3 * (2 + 5))
63
>>> productSum([2,5,[1,2]) # 2 + 5 + 2 * (1 + 2)
13
'''
# O(n(int)+n(arr)) time | O(n(arr)) space
def specialArrayProductSum(array, height = 1):
    runningSum = 0
    for el in array:
        if type(el) is list:
            runningSum += (height + 1)*specialArrayProductSum(el, height+1)
        else:
            runningSum += el
    return runningSum


def productSum(array):
    return specialArrayProductSum(array)
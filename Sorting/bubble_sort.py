# O(n^2) time | O(1) space
def bubbleSort(array):	
    for i in range(len(array), 0, -1):
        isSorted = True
        for j in range(i - 1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                isSorted = False
        if isSorted:
            break
    return array
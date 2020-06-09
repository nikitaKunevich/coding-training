def insertionSort(array):
    sorted_end = 0
    while sorted_end != len(array) - 1:
        for i in range(sorted_end + 1, 0, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            else:
                break
        sorted_end +=1
    return array

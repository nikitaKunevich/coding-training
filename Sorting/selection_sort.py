# bubble sort - compare each number and swap if different. until all numbers 'bubble up'
# to their correct position

# insertion sort - we have 2 parts - sorted and unsorted. we iterate through
# the unsorted list and find its position in the sorted array by swapping with elements in
# the sorted part

# selection sort - we define 2 array parts - sorted and unsorted. in the unsorted part
# we find the smallest number and swap it with the first elem in unsorted part until
# of the array is sorted.

def selectionSort(array):
    last_sorted = -1
    while last_sorted < len(array) - 1:
        min_idx = last_sorted + 1
        for i in range(last_sorted + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i
        array[last_sorted + 1], array[min_idx] = array[min_idx], array[last_sorted + 1]
        last_sorted += 1
        
    return array
# O(n) time
# create 2 pointers - one for back it would check if number is not 'target', 
# and in that case swap it with 'front' pointer
# front pointer tracks 'target' numbers
# [2, 1, 2, 2, 2, 3, 4, 2]
def moveElementToEnd(array, toMove):
    front = 0
    back = len(array) - 1
    while back > front:
        if array[back] == toMove:
            back-=1
        elif array[front] != toMove:
            front+=1
        else:
            array[front],array[back] = array[back],array[front]
            back-=1
            front+=1
    return array
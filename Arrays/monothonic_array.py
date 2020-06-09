# 1. go through all the array until find array's direction (if there is,
# if all elms are equal - no dir)
# 2. after direction is found finish traversal checking if direction is saved

def isMonotonic(array):
    if len(array) < 3:
        return True
    dir = 0
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        if diff > 0:
            cur_dir = 1
        elif diff == 0:
            cur_dir = 0
        else:
            cur_dir = -1
        if dir !=0:
            if cur_dir !=0 and dir != cur_dir:
                return False
        else:
            dir = cur_dir
    return True
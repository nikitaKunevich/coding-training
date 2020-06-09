# 2. 
#-3,0,4
#1,5,10

# 1. O(n^2) time | O(1) space
def smallestDifferenceSlow(arrayOne, arrayTwo):
    diff = float('inf')
    num = None
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            currDiff = abs(arrayOne[i] - arrayTwo[j])
            if currDiff < diff:
                diff = currDiff
                num = [arrayOne[i], arrayTwo[j]]
    return num

#-3(x)...1(x)..4(y).6(y).....13(x)
# 2. O(n*log(n) + m*log(m)) time | O(n+m) space
def smallestDifferenceOne(arrayOne, arrayTwo):
    merged_array = [(x, 1) for x in arrayOne] + [(y, 2) for y in arrayTwo]
    merged_array.sort()
    min_diff = float('inf')
    answer = None
    for i in range(len(merged_array) - 1):
        if merged_array[i][1] != merged_array[i+1][1]:
            one_shift = 0 if merged_array[i][1] == 1 else 1
            val_one = merged_array[i + one_shift][0]
            val_two = merged_array[i + 1 - one_shift][0]
            cur_diff = abs(val_one - val_two)
            if cur_diff < min_diff:
                min_diff = cur_diff
                answer = [val_one, val_two]
    return answer

# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifferenceTwo(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointerone = pointertwo = 0
    min_diff = float('inf')
    cur_diff = 0
    min_diff_pair = None
    while pointerone < len(arrayOne) and pointertwo < len(arrayTwo):
        num_one, num_two = arrayOne[pointerone], arrayTwo[pointertwo]
        if num_one < num_two:
            cur_diff = num_two - num_one
            pointerone += 1
        elif num_one > num_two:
            cur_diff = num_one - num_two
            pointertwo += 1
        else:	
            return [num_one,num_two]
        if cur_diff < min_diff:
            min_diff = cur_diff
            min_diff_pair = [num_one, num_two]
    return min_diff_pair

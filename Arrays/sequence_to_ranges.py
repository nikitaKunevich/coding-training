'''
Given array of non-negative integers return string with all of the intervals
in that string in sorted order for adjacent numbers or numbers otherwise.
Intervals should be separated with commas (,), start and end of interval should be
separated by hyphen (-).
e.g.:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4"
'''
def getIntervals(array):
    if len(array) == 0:
        return ""
    elif len(array) == 1:
        return str(array[0])
    array.sort() #0,1,2,3,4,5,8,9,11
    prev = array[0] #8
    out_str = str(prev) #'0-5,8'
    in_interval = False
    
    for i in range(1,len(array)): 
        if array[i] == prev + 1: #9
            in_interval = True
        else:
            #2 cases: had adjacent or didn't have
            if in_interval:
                out_str += f'-{prev},{array[i]}'
                in_interval = False
            else:
                out_str += f',{array[i]}'
        prev = array[i]
    if in_interval:
        out_str += f'-{array[-1]}'
    return out_str
assert getIntervals([1,4,5,2,3,9,8,11,0]) == '0-5,8-9,11'
assert getIntervals([1,4,3,2]) == '1-4'
assert getIntervals([1,4]) == '1,4'
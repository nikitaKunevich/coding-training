# O(n) time | O(1) space
def longestPeak(array):
    n = len(array)
    if n < 3:
        return 0
    max_len = 0
    for p in range(1, n - 1):
        l,r = p,p
        cur_len = 1
        while l - 1 >= 0 and array[l-1] < array[l]:
            cur_len+=1
            l-=1
        if l == p:
            continue
        while r + 1 < n and array[r+1] < array[r]:
            cur_len+=1
            r+=1
        if r == p:
            continue
        if cur_len >= 3 and cur_len > max_len:
            max_len = cur_len
    return max_len
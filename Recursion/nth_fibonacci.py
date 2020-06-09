# 0, 1, 1, 2, 3, 5, 8, 13, ...
# simple solution
# O(2^n) time | O(n) space
def getNthFibSimple(n):
    if n == 1: 
        return 0
    if n == 2: 
        return 1
    return getNthFibSimple(n-1) + getNthFibSimple(n-2)

######################
# O(n) time | O(n) space
cache = [0, 1]

#1st is cache[0], 2nd is cache[1]
def getNthFibMemo(n):
    if len(cache) >= n:
        return cache[n - 1]
    cache.append(getNthFibMemo(n-1) + getNthFibMemo(n-2))
    return cache[n - 1]
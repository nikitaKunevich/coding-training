# O(n^2) time | O(1) space
def longestPalindromicSubstring(s):
    n = len(s)
    if n == 1:
        return s[0]
    l,r = 0,0
    maxstr = s[0]
    maxlen = 1
    for i in range(n*2):
        il,ir = l,r
        while True:
            if (il < 0 or ir >= n) or s[il] != s[ir] :
                if ir - il - 1 > maxlen:
                    maxstr = s[il+1:ir]
                    maxlen = ir - il -1
                break
            il-=1
            ir+=1
        if i % 2 == 0:
            r +=1
        else:
            l += 1
    return maxstr

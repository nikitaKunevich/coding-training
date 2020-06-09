# O(n) time | O(1) space
def isPalindromeNoSpace(string):
    if len(string) == 1:
        return True
    left = 0
    right = len(string) - 1
    while right > left: #would work for both odd and even length
        if string[left] != string[right]:
            return False
        left += 1
        right -=1
    return True

###############################
# O(n) time | O(n) space
def isPalindromeWithStack(string):
    if len(string) == 1:
        return True
    char_stack = []
    is_odd = (len(string) % 2) == 1
    for i,el in enumerate(string):
        if is_odd and i == len(string) //2:
            continue
        if i < len(string) //2:
            char_stack.append(el)
        elif char_stack.pop() != el:
            return False
    return True
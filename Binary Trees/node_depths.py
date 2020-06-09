# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calcdepthsum(node, depth, sum):
    if node is None:
        return sum
    sum +=depth
    if node.left is None and node.right is None:
        return sum
    sum = calcdepthsum(node.left, depth+1, sum)
    sum = calcdepthsum(node.right, depth+1, sum)
    return sum

# O(n) time | O(n) space (worst)
def nodeDepthsOne(root):
    return calcdepthsum(root, 0, 0)

################################################################################
def nodeDepthsTwo(root):
    # Write your code here.
    stack = [(root, 0)]
    sum = 0
    while len(stack) > 0:
        node, depth = stack.pop()
        if node is None:
            continue
        sum+=depth
        stack.append((node.left, depth+1))
        stack.append((node.right, depth+1))
    return sum

################################################################################

def recursivelyCalcDepths(node, depth=0):
    if node is None:
        return 0
    return depth + recursivelyCalcDepths(node.left,depth+1) + recursivelyCalcDepths(node.right,depth+1)

def nodeDepthsThree(root):
    # Write your code here.
    return recursivelyCalcDepths(root)
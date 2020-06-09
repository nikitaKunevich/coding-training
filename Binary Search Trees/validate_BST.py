# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return helperValidateBST(tree, float('-inf'), float('inf'))

# O(n) time | O(n) space
def helperValidateBST(node, min, max): # (12, 13, 16)
    if node is None:
        return True

    if node.value < min or node.value >= max:
        return False
 
    if not helperValidateBST(node.left, min, node.value):
         return False

    return helperValidateBST(node.right, node.value, max)   

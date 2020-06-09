# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space worst | O(log(n)) space average
def TraverseBSTAndSumOne(node, sum_array, current_sum):
    current_sum += node.value
    if node.left is None and node.right is None:	
        sum_array.append(current_sum)
        return sum_array
    if node.left is not None:
        TraverseBSTAndSumOne(node.left, sum_array, current_sum)
    if node.right is not None:
        TraverseBSTAndSumOne(node.right, sum_array, current_sum)
    return sum_array


def branchSumsOne(root):
    return TraverseBSTAndSumOne(root, [], 0)

################################################################################

# O(n) time | O(n) space worst | O(log(n)) space average
def TraverseBSTAndSumTwo(node, sums, running_sum):
    if node is None:
        return
    running_sum += node.value
    if node.left is None and node.right is None:
        sums.append(running_sum)
        return
    TraverseBSTAndSumTwo(node.left, sums, running_sum)
    TraverseBSTAndSumTwo(node.right, sums, running_sum)

def branchSumsTwo(root):
    sums = []
    TraverseBSTAndSumTwo(root, sums, 0)
    return sums
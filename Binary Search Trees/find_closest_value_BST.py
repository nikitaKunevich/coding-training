# O(log(n)) time | O(1) space
def findClosestValueInBstOne(tree, target):
    closest = float("inf")
    node = tree
    while node is not None:
        if abs(node.value - target) < abs(closest - target):
            closest = node.value
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right
        else:
            break
    
    return closest

#recursively, O(n) time | O(n) space
def findClosestValueInBstTwo(tree, target):
    return recSearch(tree, None, target)

def recSearch(node, closest, target):
    if node is None:
        return closest
    if node.value == target:
        return target
    #update_closest
    if closest is None or abs(node.value - target) < abs(closest - target):
        closest = node.value
    if target < node.value:
        closest = recSearch(node.left, closest, target)
    else:
        closest = recSearch(node.right, closest, target)
    return closest


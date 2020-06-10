from typing import List

class Solution:
    # O(n) time | O(n) space 
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        if len(root.children) == 0: # if don’t have children
            return [root.val]
        results = []
        for child in root.children:
            results += self.postorder(child)
        results.append(root.val)
        return results
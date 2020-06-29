class LinkedListNode:
    def __init__(self, val = 0, next=None):
        self.next = next
        self.val = val

# O(n) time | O(1) space
def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
        
    #init, reverse first 2 links
    left = head
    cur = left.next
    right = cur.next
    head.next = None
    cur.next = head
    
    while right is not None:
        left = cur
        cur = right
        right = right.next
        
        #reverse link
        cur.next = left
    return cur
    
# O(n) time | O(1) space
def simple_reverse_linked_list(head):
    if not head:
        return head
    
    left, cur = None, head
    while cur:
        temp = cur.next
        cur.next = left
        left = cur
        cur = temp
    return left

def build_linked_list(n):
    last = None
    for i in range(n):
        last = LinkedListNode(i, last)
    return last

def traverse_linked_list(head):
    node = head
    out = []
    while node is not None:
        out.append(node.val)
        node = node.next
    return out or None



def validate_linked_list(head, array):
    assert traverse_linked_list(head) == array
    head = simple_reverse_linked_list(head)
    assert traverse_linked_list(head) == (None if array is None else list(reversed(array)))

validate_linked_list(build_linked_list(0),None)
validate_linked_list(build_linked_list(1),[0])
validate_linked_list(build_linked_list(2),[1,0])
validate_linked_list(build_linked_list(10),list(reversed(range(10))))
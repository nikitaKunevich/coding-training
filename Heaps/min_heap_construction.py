# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.

# recursive solution
def swap(array, first, second):
    array[first], array[second] = array[second], array[first]

class MinHeapOne:
    def __init__(self, array):
        # Do not edit the line below.
        self.buildHeap(array)
    
    @staticmethod
    def getParent(idx):
        return (idx - 1)//2
        
    @staticmethod
    def getChildren(idx):
        return (2*idx + 1, 2*idx + 2)
    
    def buildHeap(self, array):
        self.heap = array
        
        firstParentIdx = self.getParent(len(array) - 1)
        for i in reversed(range(firstParentIdx + 1)):
            self.siftDown(i)
        return self.heap
        
    def siftDown(self, idx):
        #check if children
        child_idx, child2_idx = self.getChildren(idx)
        
        if child_idx > len(self.heap) - 1:
            # no children
            return
        if child2_idx > len(self.heap) - 1:
            # only one child
            if self.heap[idx] > self.heap[child_idx]:
                swap(self.heap, idx, child_idx)
        else:
            #two children
            if (self.heap[child_idx] < self.heap[idx] and
            self.heap[child_idx] <= self.heap[child2_idx]):
                swap(self.heap, idx, child_idx)
                self.siftDown(child_idx)
            elif (self.heap[child2_idx] < self.heap[idx] and
            self.heap[child2_idx] <= self.heap[child_idx]):
                swap(self.heap, idx, child2_idx)
                self.siftDown(child2_idx)

    def siftUp(self, idx):
        parentIdx = self.getParent(idx)
        if parentIdx < 0:
            return
            
        if self.heap[idx] < self.heap[parentIdx]:
            swap(self.heap, idx, parentIdx)
            self.siftUp(parentIdx)

    def peek(self):
        return self.heap[0]

    def remove(self):
        if len(self.heap) == 0:
            return
        if len(self.heap) == 1:
            return self.heap.pop()
        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDown(0)
        return res

    def insert(self, value):
        # insert new value at the end and sift it up
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

##############################################

class MinHeapTwo:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array[:]
        firstParentIdx = (len(array) - 2) // 2
        for i in reversed(range(firstParentIdx + 1)):
            self._siftDown(i)
        return self.heap

    def _siftDown(self, currentIdx):
        lastElement = len(self.heap) - 1
        lastParent = (lastElement - 1) // 2
        # how to check for ending condition
        while currentIdx <= lastParent:
            firstChild = currentIdx * 2 + 1
            secondChild = firstChild + 1 if firstChild + 1 <= lastElement else -1
            if secondChild == -1 or self.heap[firstChild] <= self.heap[secondChild]:
                childToSwap = firstChild
            else:
                childToSwap = secondChild
            if self.heap[childToSwap] < self.heap[currentIdx]:
                swap(self.heap, childToSwap, currentIdx)
                currentIdx = childToSwap
            else:
                break
                
    # O(n) time | O(1) space
    def _siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx] < self.heap[parentIdx]:
                swap(self.heap, currentIdx, parentIdx)
                currentIdx = parentIdx
            else:
                break

    def peek(self):
        return self.heap[0]

    def remove(self):
        swap(self.heap, 0, len(self.heap) - 1)
        removedValue = self.heap.pop()
        self._siftDown(0)
        return removedValue

    def insert(self, value):
        self.heap.append(value)
        self._siftUp(len(self.heap) - 1)

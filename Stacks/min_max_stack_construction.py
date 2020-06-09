class StackElement:
    def __init__(self, value, min, max):
        self.value = value
        self.min = min
        self.max = max

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        
    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.stack[-1].value
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def _get_last_elem(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
        
    def pop(self):
        #update min and max
        if self.is_empty():
            raise IndexError
        return self.stack.pop().value

    def push(self, number):
        prev_elm = self._get_last_elem()
        if prev_elm is None:
            new_min = new_max = number
        else:
            new_min, new_max = prev_elm.min, prev_elm.max
            if prev_elm.min > number:
                new_min = number
            elif prev_elm.max < number:
                new_max = number
        self.stack.append(StackElement(number, new_min, new_max))

    def getMin(self):
        if self.is_empty():
            raise IndexError
        return self._get_last_elem().min

    def getMax(self):
        if self.is_empty():
            raise IndexError
        return self._get_last_elem().max

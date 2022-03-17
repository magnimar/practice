from array_deque import ArrayDeque

class Stack:
    def __init__(self):
        self.container = ArrayDeque()

    def push(self, data):
        self.container.push_back(data)
    
    def pop(self):
        temp_val = self.container.pop_back()
        return temp_val
    
    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return self.container.__str__()
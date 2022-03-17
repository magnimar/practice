from my_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.container = LinkedList()

    def add(self, data):
        self.container.push_back(data)
    
    def remove(self):
        temp_val = self.container.pop_front()
        return temp_val

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return self.container.__str__()
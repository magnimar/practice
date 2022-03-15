from os import remove


class Node:    
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, head = None, tail = None, size = 0, curr_pos = None):
        self.head = Node("head", None, None)
        self.tail = Node("tail", None, self.head)
        self.head.next = self.tail
        self.current_node = self.tail
        self.current_pos = 0
        self.size = 0

    def __str__(self):
        return_str = " "
        var = self.head
        while var:
            return_str += str(var.data) + " "
            var = var.next
        return return_str

    def __len__(self):
        return self.size

    def insert(self, value):
        new_node = Node(value, self.current_node, self.current_node.prev)
        self.current_node.prev.next = new_node
        self.current_node.prev = new_node
        self.current_node = new_node
        self.size += 1

    def remove(self):
        self.current_node.prev.next = self.current_node.next
        self.current_node.next.prev = self.current_node.prev
        self.size -= 1
        if self.current_pos ==  0:
           self.current_node = self.current_node.next 
           return
        self.current_node = self.current_node.prev

    def get_value(self):
        return self.current_node.data

    def move_to_next(self):
        if self.size-1 == self.current_pos:
            return
        self.current_pos += 1
        self.current_node = self.current_node.next

    def move_to_prev(self):
        if self.current_pos == 0:
            return
        self.current_pos -= 1
        self.current_node = self.current_node.prev

    def move_to_pos(self, position):
        if self.current_pos == position:
            return
        if position < 0 or position > self.size -1:
            return
        if position < self.current_pos:
            self.current_pos = self.current_pos-1
            self.current_node = self.current_node.prev
            return self.move_to_pos(position)
        if self.current_pos < position:
            self.current_pos = self.current_pos + 1
            self.current_node = self.current_node.next
            return self.move_to_pos(position)

    def remove_all(self, value):
        original_node = self.current_node
        self.move_to_pos(0)
        if_same = False
        while self.current_node:
            if self.current_node.data == value:
                if self.current_node == original_node:
                    if_same = True
                self.remove()
            else:
                self.current_node = self.current_node.next
        if if_same == True:
            self.current_node = self.head.next
            self.current_pos = 0
        else:
            self.current_node = original_node

    def reverse(self):
        self.move_to_pos(0)
        walk_back = self.current_node
        while walk_back:

    def sort():
        pass

dll = DLL()
dll.insert("a")
dll.insert("b")
dll.insert("c")
dll.insert("d")
dll.insert("e")
dll.insert("f")
dll.insert("g")
dll.insert("g")
dll.move_to_pos(2)
dll.remove_all("f")
print(dll)
print(dll.current_node.data)
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0

    def __str__(self) -> str:
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data)+" "
            node = node.next
        return ret_str

    def push_front(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head
            self.size += 1
    
    def pop_front(self):
        if self.size == 0:
            return None
        old_head = self.head.data
        self.head = self.head.next
        self.size -= 1
        return old_head

    def push_back(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def pop_back(self):
        if self.head == None:
            return None
        if self.size == 1:
            temp_val = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return temp_val.data
        last = self.head
        while (last.next.next):
            last = last.next
        temp_val = last.next
        last.next = None
        self.tail = last
        self.size -= 1
        return temp_val.data      

    def get_size(self):
        return self.size
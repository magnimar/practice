class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:
    def __init__(self, key=None, value=None, next=None):
       self.key = key
       self.value = value
       self.next = next

class Bucket:
    def __init__(self):
        self.head = None

    def __len__(self):
        if self.head == None:
            return 0
        return self.len_help(self.head)

    def __str__(self):
        if self.head == None:
            return ""
        return self.str_help(self.head)

    def ultimate_finder(self, key):
        if self.head == None:
            return None
        return self.ultimate_finder_helper(key, self.head)

    def ultimate_finder_helper(self, key, node):
        if node == None:
            return None
        if node.key == key:
            return node
        return self.ultimate_finder_helper(key, node.next)
        
    def str_help(self, node):
        if node.next == None:
            return " ( {} : {} ) ".format(node.key, node.value)
        return " ( {} : {} ) ".format(node.key, node.value) + self.str_help(node.next)

    def len_help(self, node):
        if node == None:
            return 0
        return 1 + self.len_help(node.next)

    def insert(self, key, data):
        if self.head == None:
            self.head = Node(key, data)
            return
        find = self.ultimate_finder(key)
        if find:
            raise ItemExistsException("item already exists")
        new_node = Node(key, data)
        old_head = self.head
        self.head = new_node
        self.head.next = old_head

    def update(self, key, value):
        find = self.ultimate_finder(key)
        if find:
            return find.value
        else:
            raise NotFoundException("item not found")

    def find(self, key):
        find = self.ultimate_finder(key)
        if find:
            return find.value
        else:
            return NotFoundException("item not found")

    def contains(self, key):
        find = self.ultimate_finder(key)
        if find:
            return True
        return False

    def remove(self, key):
        self.head = self.remove_help(key, self.head)

    def remove_help(self, key, node):
        if node == None:
            raise NotFoundException("item not found")
        if node.key == key:
            return node.next
        node.next = self.remove_help(key, node.next)
        return node

    def __setitem__(self, key, data):
        find = self.ultimate_finder(key)
        if find:
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        find = self.ultimate_finder(key)
        if find:
            return find.key
        else:
            raise NotFoundException("item not found")

class HashMap:
    def __init__(self):
        self.size = 0
        self.lis_size = 4
        self.array = [None] * self.lis_size
        for i in range(len(self.array)):
            self.array[i] = Bucket()

    def __str__(self):
        return_str = ""
        for i in range(self.lis_size):
            if self.array[i]:
                return_str += "nr: {} contains: {}\n".format(i, self.array[i])
            else:
                return_str += "nr: {} is empty \n".format(i)
        return return_str

    def insert(self, key, value):
        self.resize()
        val_hash = hash(key) % self.lis_size
        self.array[val_hash].insert(key, value)
        self.size += 1

    def update(self, key, value):
        val_hash = hash(key) % self.lis_size
        self.array[val_hash].update(key, value)

    def find(self, key):
        val_hash = hash(key) % self.lis_size
        return self.array[val_hash].find(key)

    def contains(self, key):
        val_hash = self.hash(key) % self.lis_size
        return self.array[val_hash].contains(key)

    def remove(self, key):
        val_hash = hash(key) % self.lis_size
        self.array[val_hash].remove(key)
        self.size -= 1

    def __setitem__(self, key, data):
        val_hash = hash(key) % self.lis_size
        if self.array[val_hash].contains(key):
            self.array[val_hash].update(key, data)
        else:
            self.array[val_hash].insert(key, data)
            self.size += 1

    def __getitem__(self, key):
        val_hash = hash(key) % self.lis_size
        return self.array[val_hash].__getitem__(key)

    def __len__(self):
        counter = 0
        for i in range(len(self.array)):
            counter += self.array[i].__len__()
        return counter

    def resize(self):
        if self.size > 1.2*self.lis_size:
            self.lis_size *= 2
            temp = [None] * self.lis_size
            for i in range(len(temp)):
                temp[i] = Bucket()
            temp2 = temp
            temp = self.array
            self.array = temp2
            self.size = 0
            for i in range(len(temp)):
                bucket = temp[i]
                node = bucket.head
                while node:
                    self.insert(node.key, node.value)
                    node = node.next

hm = HashMap()
hm.insert(1, 10)
hm.insert(2, 20)
hm.insert(3, 30)
hm.insert(4, 40)
hm.insert(5, 50)
print(hm)
hm.insert(6, 60)
print(hm.lis_size, "lis size")
print(hm)
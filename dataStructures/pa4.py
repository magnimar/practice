class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class BSTMapNode:
    def __init__(self, key=None, value=None, right=None, left=None):
        self.data = {}
        self.data[key] = value
        self.left = left
        self.right = right
 
class BSTMap:
    def __init__(self, root=None):
        self.root = root

    def print(self):
        self.print_recur(self.root, 0)

    def print_recur(self, node, indent_level):
        if node == None or node.data==None:
            return
        indent_level += 1
        self.print_recur(node.left, indent_level)
        print("\t"*indent_level + str(node.data))
        self.print_recur(node.right, indent_level)
    
    def insert(self, key, value):
        if self.root == None:
            self.root = BSTMapNode(key, value)
            return
        self.insert_helper(self.root, key, value)

    def insert_helper(self, node, key, value):
        curr_key = list(node.data.keys())[0]
        if curr_key > key:
            if node.left:
                self.insert_helper(node.left, key, value)
            else:
                node.left = BSTMapNode(key, value)
        if curr_key < key:
            if node.right:
                self.insert_helper(node.right, key, value)
            else:
                node.right = BSTMapNode(key, value)
        if curr_key == key:
            raise ItemExistsException("Item already exists")

    def ultimate_finder(self, key):
        return self.ultimate_finder_helper(self.root, key)

    def ultimate_finder_helper(self, node, key):
        if node == None:
            return None
        curr_key = list(node.data.keys())[0]
        if curr_key == key:
            return node
        if curr_key > key:
            return self.ultimate_finder_helper(node.left, key)
        if curr_key < key:
            return self.ultimate_finder_helper(node.right, key)

    def update(self, key, value):
        node = self.ultimate_finder(key)
        if node:
            node.data[key] = value
        else:
            NotFoundException("Item not found")

    def find(self, key):
        finder = self.ultimate_finder(key)
        if finder:
            return finder.data[key]
        raise NotFoundException("Item not found")

    def contains(self, key):
        if self.ultimate_finder(key):
            return True
        return False

    def remove(self, key):
        self.root = self.remove_recur(key, self.root)

    def remove_recur(self, key, node):
        if node == None:
            raise NotFoundException("item not foound")
        if key < list(node.data.keys())[0]:
            node.left = self.remove_recur(key, node.left)
            return node
        if list(node.data.keys())[0] < key:
            node.right = self.remove_recur(key, node.right)
            return node
        if node.right == None and node.left == None:
            return None
        if node.right == None and node.left:
            return node.left
        if node.left == None and node.right:
            return node.right
        if node.left and node.right:
            temp = self.find_left_replace_node(node.left)
            node.data = temp.data
            node.left = self.remove_recur(list(temp.data.keys())[0], node.left)
            return node

    def find_left_replace_node(self, node):
        print(node.data, "left repl")
        if node.right ==None:
            return node
        return self.find_left_replace_node(node.right)

    def __setitem__(self, key, value):
        find = self.ultimate_finder(key)
        if find:
            self.update(key, value)
        else:
            self.insert(key, value)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.len_help(self.root)

    def len_help(self, node):
        if node==None:
            return 0
        left = self.len_help(node.left)
        right = self.len_help(node.right)
        return 1 + left + right

    def __str__(self):
        return self.str_recur(self.root)

    def str_recur(self, node, final_str=""):
        if node == None or node.data==None:
            return ""
        left = self.str_recur(node.left)
        right = self.str_recur(node.right)
        return left + str(node.data) + " " + right

b = BSTMap()
b.insert(6, 10)
b.insert(3, 10)
b.insert(10, 10)
b.insert(1, 10)
b.insert(7, 10)
b.insert(9, 10)
b.insert(2, 10)
print(b.print())
class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:

    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
        self.ordered = True

    def __str__(self):
        return_str = " "
        for i in range(self.size):
            return_str += str(self.arr[i])
        return return_str

    def prepend(self, value):
        self.ordered = False
        self.insert(value,0)

    def insert(self, value, index):
        self.ordered = False
        if self.size == self.capacity:
            self.resize()
        if index < 0 or self.size < index:
            raise IndexOutOfBounds("index error")
        for i in range(self.size-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = value
        self.size += 1

    def append(self, value):
        self.ordered = False
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def set_at(self, value, index):
        self.ordered = False
        self.arr[index] = value

    def get_first(self):
        if self.arr[0] == None:
            raise Empty()
        else:
            print(self.arr[0])

    def get_at(self, index):
        if index < 0 or self.size <= index:
            raise IndexOutOfBounds()
        else:
            print(self.arr[index])

    def get_last(self):
        if self.arr[self.size-1] == None:
            raise Empty()
        else:
            print(self.arr[self.size-1])

    def resize(self):
        self.capacity *= 2
        temp_arr = [None] * self.capacity
        for i in range(self.size):
            temp_arr[i] = self.arr[i]
        self.arr  = temp_arr

    def remove_at(self, index):
        if index < 0 or self.size < index:
            raise IndexOutOfBounds("index error")
        for i in range(index, self.size, 1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.size] = None
        self.size -= 1

    def clear(self):
        self.ordered = True
        self.arr = [None] * self.capacity
        self.size = 0

    def insert_helper(self, value, index):
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = value
        self.size += 1

    def insert_ordered(self, value):
        if not self.ordered:
            raise NotOrdered("the list is not ordered")
        if self.size == self.capacity:
            self.resize()
        if self.size == 0:
            self.insert_helper(value, 0)
        elif self.size == 1:
            if self.arr[0] < value:
                self.insert_helper(value, 1)
            else:
                self.insert_helper(value, 0)
        else:
            i = self.size - 1
            while i > 0:
                if self.arr[i] < value:
                    self.insert_helper(value, i+1)
                    break
                else:
                    i -= 1
            
    def find(self, value):
        if self.ordered == True:
            return self.find_ordered(value)
        if self.ordered == False:
            return self.find_not_ordered(value)

    def binary_s_help(self, lis, low, high, value):
        if low == high:
            if lis[low] == value:
                return low
            else:
                return "num not in list"
        mid = (high+low) // 2 
        if lis[mid] == value:
            return mid
        elif lis[mid] < value:
            return self.binary_s_help(lis, mid, high, value)
        else:
            return self.binary_s_help(lis, low, mid, value)

    def find_ordered(self, value):
        lis = self.arr
        if lis == []:
            return False
        mid = self.size // 2
        if lis[mid] == value:
            return mid
        elif lis[mid] < value:
            return self.binary_s_help(lis, mid, self.size, value)
        else:
            return self.binary_s_help(lis, 0, mid, value)
                

    def find_not_ordered(self, value):
        for i in range(0,self.size):
            if value == self.arr[i]:
                return i
        return False

    def remove_value(self, value):
        index = self.find(value)
        self.remove_at(index)

if __name__ == "__main__":

    arr_lis = ArrayList()
    arr_lis.insert_ordered(10)
    arr_lis.insert_ordered(20)
    arr_lis.insert_ordered(30)
    arr_lis.insert_ordered(25)
    arr_lis.insert_ordered(50)
    arr_lis.insert_ordered(35)
    arr_lis.insert_ordered(15)
    print(arr_lis.arr)
    print(arr_lis.ordered)
    print(arr_lis.size)
    arr_lis.remove_value(30)
    print(arr_lis.arr)

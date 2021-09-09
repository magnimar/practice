class IndexOutOfBounds(Exception):   #if the requested index is out of bounds
    pass

class NotFound(Exception):   #if something is not found
    pass

class Empty(Exception):   #if something is empty
    pass

class NotOrdered(Exception):   #if something is not in order
    pass

class ArrayList:

    def __init__(self):
        self.capacity = 4   #the length of the actual list
        self.arr = [None] * self.capacity   #after the list there is filler to fill the capacity
        self.size = 0    #kepps track of the length of the list
        self.ordered = True   #tells us whether the list in question is ordered or not

    def __str__(self):   #prints out the string of the list
        return_str = ""
        if self.size == 0:
            return ""
        else:
            for i in range(self.size-1):
                return_str += str(self.arr[i]) + ", "
            return return_str + str(self.arr[self.size-1])

    def prepend(self, value):   #adds a value to the front and moves all the other values
        self.ordered = False
        self.insert(value, 0)

    def insert(self, value, index):   #inserts a value at a specific index and moves the values that come after
        self.ordered = False
        if self.size == self.capacity:
            self.resize()
        if index < 0 or self.size < index:
            raise IndexOutOfBounds()
        for i in range(self.size-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = value
        self.size += 1

    def append(self, value):   #adds a value to the back of a list
        self.ordered = False
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def set_at(self, value, index):   #change the value at a specific index
        self.ordered = False
        if index < 0 or self.size <= index:
            raise IndexOutOfBounds()
        if self.size == 0:
            raise IndexOutOfBounds()
        self.arr[index] = value

    def get_first(self):    #prints the first value
        if self.arr[0] == None:
            raise Empty()
        else:
            return self.arr[0]

    def get_at(self, index):    #prints the value at a specific index
        if index < 0 or self.size <= index:
            raise IndexOutOfBounds()
        else:
            return self.arr[index]

    def get_last(self):    #prints the last value of a list
        if self.arr[self.size-1] == None:
            raise Empty()
        else:
            return self.arr[self.size-1]

    def resize(self):    #doubles the capacity of a list 
        self.capacity *= 2
        temp_arr = [None] * self.capacity
        for i in range(self.size):
            temp_arr[i] = self.arr[i]
        self.arr  = temp_arr

    def remove_at(self, index):    #removes the value at a specific index and moves all the other values to fill in
        if index < 0 or self.size <= index:
            raise IndexOutOfBounds()
        for i in range(index, self.size-1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.size-1] = None
        self.size -= 1

    def clear(self):    #clears the list so that all items are blank
        self.ordered = True
        self.arr = [None] * self.capacity
        self.size = 0

    def insert_helper(self, value, index):    #inserts a value at a specific index and keeps it ordered
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = value
        self.size += 1

    def insert_ordered(self, value):    #inserts a value at the correct place in a ordered list
        if not self.ordered:
            raise NotOrdered()
        if self.size == self.capacity:
            self.resize()
        if self.size == 0:
            return self.insert_helper(value, 0)   #if the list is empty then insert at index 0
        if self.size == 1:
            if self.arr[0] < value:
                return self.insert_helper(value, 1)   #if the list has one value and it is smaller than the value to insert, the value to insert goes to index 1
            else:
                return self.insert_helper(value, 0)   #if the list has one value and it is bigger than the value to insert, value to insert at index 0
        else:
            i = self.size - 1
            while i > -1:
                if self.arr[i] < value:
                    self.insert_helper(value, i+1)    #iterates backwards through a list and when it encounter a value that is smaller then it is inserted one index higher
                    break
                if i==0:
                    self.insert_helper(value, 0)   #if none of the items are smaller than the value to insert, then it goes into index 0
                    break
                else:
                    i -= 1
            
    def find(self, value):    #find a value in a list, simpler for the user
        if self.ordered == True:
            return self.find_ordered(value)   #if the list is ordered
        if self.ordered == False:
            return self.find_not_ordered(value)   #if list is not ordered

    def find_ordered(self, value):
        return self.binary_search(self.arr, 0, self.size-1, value)   #calls a binary search function if it is ordered

    def binary_search(self, lis, low, high, value):   #binary search function
        if low == high:     #if there is only one index left to check
            if lis[low] == value:  #if the last index left is the value
                return low
            else:
                return NotFound("Value not found in list")   #if the last index to check is not the value, then not found
        middle = (low+high) // 2
        if lis[middle] == value:    #if the middle index is the value
            return middle
        elif lis[middle] < value:
            return self.binary_search(lis, middle+1, high, value)   #if the middle is lower than the value then the function is called again with another range to check
        else:
            return self.binary_search(lis, 0, middle, value)    #if the middle is higher than the value then the function is called again with a new range

    def find_not_ordered(self, value):    #a linear search to check an unordered list
        for i in range(0, self.size-1):
            if self.arr[i] == value:
                return i
        return "Value not found in list"

    def remove_value(self, value):    #removes a value from a list
        index = self.find(value)
        self.remove_at(index)

if __name__ == "__main__":
    
    arr_lis = ArrayList()
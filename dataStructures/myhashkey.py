class MyHashableKey:
    def __init__(self, int_value, str_value):
        self.int_value = int_value
        self.str_value = str_value

    def __eq__(self, other):
        if self.int_value == other.int_value:
            return  self.str_value == other.str_value
        return False

    def __hash__(self):
        pos_int = self.int_value * 983
        pos_int = pos_int % 311
        pos_int = pos_int % 79
        total = 0
        for i in range(len(self.str_value)):
            total += ord(self.str_value[i]) * (i+1)
        return int(pos_int+total)
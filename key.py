class MyComparableKey:
    def __init__(self, int_value, str_value):
        self.int_value = int_value
        self.str_value = str_value

    def __str__(self):
        return str(list(self.dict.keys())[0])

    def __lt__(self, other):
        if self.int_value == other.int_value:
            return self.str_value < other.str_value
        return self.int_value < other.int_value
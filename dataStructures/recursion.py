from typing import Counter


def modulus(num1, num2):
    if num1 >= num2:
        return modulus(num1-num2, num2)
    else:
        return num1

#print(modulus(13, 4))
#print(modulus(12, 3))
#print(modulus(14, 3))

def how_many(lis1, lis2):
    return how_many_recursive(lis1, lis2, 0, 0)

def how_many_recursive(lis1, lis2, idx1, idx2):
    if idx2 == len(lis2):
        return how_many_recursive(lis1, lis2, idx1+1, 0)
    if idx1 == len(lis1):
        return 0
    if lis1[idx1] == lis2[idx2]:
        return 1 + how_many_recursive(lis1, lis2, idx1+1, 0)
    else:
        return how_many_recursive(lis1, lis2, idx1, idx2+1)

print(how_many(["a","f","d","t"],["a","b","c","d","e"]))
print(how_many(["a","b","f","g","a","t","c"],["a","b","c","d","e", "a"]))
def modulus(num1, num2):  #calculates the modulus of num1 with respect to num2 recursively
    if num1 >= num2:
        return modulus(num1-num2, num2)
    else:
        return num1


def how_many(lis1, lis2):   #checks how many items in lis1 are also in lis2 recursively by taking 2 lists as input and using another function to simplify the user experience
    return how_many_recursive(lis1, lis2, 0, 0)

def how_many_recursive(lis1, lis2, idx1, idx2):   #checks every index in lis1 for all indexes in lis2 and then moves on to the next index in lis2
    if idx2 == len(lis2):
        return how_many_recursive(lis1, lis2, idx1+1, 0)   #if all the indexes in lis2 have been checked the function returns to the next index in lis1
    if idx1 == len(lis1):   #if all the indexes in lis1 have been checked the function is complete and returns
        return 0
    if lis1[idx1] == lis2[idx2]:
        return 1 + how_many_recursive(lis1, lis2, idx1+1, 0)   #if the indexes have the same value the function returns 1 and continues
    else:
        return how_many_recursive(lis1, lis2, idx1, idx2+1)   #if the indexes do not match it simply goes on to the next index in lis2

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])


if __name__ == "__main__":
    run_recursion_program()
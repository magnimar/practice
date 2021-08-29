'''
The following code is a practice in recursion, its utility is to take in a list and using recursion; find the max and min of the list. It was also a practice in time complexity because each recursion needs to take a minimal amount of time. 
'''

import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000)   #change recursion depth in order to test it for bigger numbers

def find_max_min(seq):   #function takes in a list of numbers
    if len(seq) == 2:   #if the function only has 2 objects left in the list then it stops and returns the min and max of the list
        if seq[0] < seq[1]:   #the lower number of the 2 is set as the min and the higher is max
            return "min is " + str(seq[0]) + " max is " + str(seq[1])
        else:
            return "min is " + str(seq[1]) + " max is " + str(seq[0])   
    elif len(seq) > 2:   #the following is executed if there are more than 2 items left in the list
        if seq[-2] < seq[-1] < seq[-3] or seq[-3] < seq[-1] < seq[-2]:   #if item at index -1 is higher than -2 but lower than -3, in the middle, then it is removed
            seq.pop(-1)   #item is removed
            return find_max_min(seq)   #the list is called again into the same function with the medium item removed
        elif seq[-1] < seq[-3] < seq[-2] or seq[-2] < seq[-3] < seq[-1]:   #does the same but for index -3
            seq.pop(-3)
            return find_max_min(seq)
        elif seq[-3] < seq[-2] < seq[-1] or seq[-1] < seq[-2] < seq[-3]:   #also the same but for index -2
            seq.pop(-2)
            return find_max_min(seq)

'''
one thing to note after this function is that the list is indexed at the back of the list to reduce the time complexity, .pop() takes shorter the closer the index is to the back of the list
'''

list_object_1 = [5, 66, 33, 7, 7, 45, 7, 2, 99999999, 655, 63433, -3, 8484848484884]
list_object_2 = [5, 432, 26, 5, -3, 4, 1, 3564635, 33, -66666]
list_object_3 = [-238479058, 444, 2, 6, 0, 1, 4523, 3]   #create three test lists

print(find_max_min(list_object_1))
print(find_max_min(list_object_2))
print(find_max_min(list_object_3))   #the lists are tested and they work!

length = 1
times = []
ns = []

while length < 20000:                           #this while loop is to test the time complexity of the list
    t0 = time.process_time()                    #logs the time it takes to run the function
    find_max_min([i for i in range(length)])    #using list comprehension a bigger and bigger list is thrown into the function
    times.append(time.process_time() - t0)      #the difference in the process time for the function and the process time before is appended to a list
    ns.append(length)                           #the length of the list that is used in the function is appended to a list
    length *= 2                                 #the length of the list thrown in is doubled

plt.plot(ns, times)    #a plot to show the time complexity for the operation
plt.xlabel('n')
plt.ylabel('f(n)')
plt.show()             #here we can see that the time complexity is O(n)
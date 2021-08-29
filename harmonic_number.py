'''
the following program has 2 ways of calculating the n-th harmonic number, one is using a for-loop and the other using recursion
'''

import time
import matplotlib.pyplot as plt

def harmonic_number(n):                 #this function uses a for-loop
    harmonic_list = []
    for i in range(n):
        harmonic_list.append(1/(i+1))   #1/n is added for each index to a list
    return sum(harmonic_list)           #the function return the sum of the list
        
def harmonic_recursive(n):             #this function uses recursion
    if n==1:                           #the first harmonic number is 1
        return 1
    else:
        return (1/n) + harmonic_recursive(n-1)   #otherwise it returns 1/n + what the function returns one number below the current one

num = 1
times = []
ns = []

while num < 999:                           #the function plots the time complexity of harmonic_recursive for a growing n
    t0 = time.process_time()                    
    harmonic_recursive(num)    
    times.append(time.process_time() - t0)      
    ns.append(num)                           
    num += 2                                 

plt.plot(ns, times)                  #on this plot we can see that the time complexity for the recursive function is O(n)
plt.xlabel('n')
plt.ylabel('f(n)')
plt.show()             

num2 = 1
times2 = []
ns2 = []

while num2 < 10000:                           #this function plots the growth of the harmonic_number with a growing n
    t0 = time.process_time()                    
    harmonic_number(num2)    
    times2.append(time.process_time() - t0)      
    ns2.append(num2)                           
    num2 += 2                                 

plt.plot(ns2, times2)                #on this plot we can see that the time complexity is O(n) for the for-loop function
plt.xlabel('n')
plt.ylabel('f(n)')
plt.show()             
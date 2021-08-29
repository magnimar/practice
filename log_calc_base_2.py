'''
this program is a practice in recursion, using recursion the program calculates the log base 2 of a number
'''

def log_calc(n):                                  
    if n==0:                                     #if the power is 0 then the function returns 0 as 2**0 = 1
        return 1
    elif n==1:                                   #if the power is 1 then the function return 1 as 2**1 = 2 
        return 2
    else:
        return log_calc(n-1) + log_calc(n-1)     #if the power is bigger, then the function calls on itself to add the result of the power below to itself 

print(log_calc(8))
print(log_calc(13))
print(log_calc(20))   #here the function is tested and it works!
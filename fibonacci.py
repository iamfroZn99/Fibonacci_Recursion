'''
 0, 1, 1, 2, 3, 5, 8, 13............
 0, 1, 2, 3, 4, 5, 6, 7........
 

 fib(1) = 1
 fib(2) = fib(0) + fib(1)
 fib(3) = fib(1) + fib(2)

 fib(n) = fib(n-2) + fib(n-1)
'''

def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n<0):
        return("Fibonacci series is not defined for negative numbers")
    
    else:
        return(fib(n-1) + fib(n-2))
         
              
print(fib(-1))
print(fib(5))
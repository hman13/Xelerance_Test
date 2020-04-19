def Fibonacci(n): 
    
    initial = 0
    curr_num = 1
    sum = 0

    while curr_num < n:
        if curr_num%2!=0:
            sum+=curr_num
        
        curr_num+=initial
        initial= curr_num-initial

    return sum    

print (Fibonacci(22))    
def fibonacci(n):
    if n <=0:
        raise ValueError("input must be positive")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("enter number: "))

sequence=fibonacci(n)

print("the",n,"th fibonacci number is",fibonacci(n))

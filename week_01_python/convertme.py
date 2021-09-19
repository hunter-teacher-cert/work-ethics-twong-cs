#factorial function
def factorial(n):
    prod = 1
    for i in range(n,1,-1):
        prod = prod * i
    return prod

#fib function
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#printing out the good news
print('Good News Everyone!')
print('1! = ' + str(factorial(1)))
print('fib(1) = ' + str(fib(1)))

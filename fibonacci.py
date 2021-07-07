# function for nth Fibonacci number

def Fibonacci(n):
    '''takes in a number, and returns its Fibonacci number'''

    if n < 0:
        print('Incorrect Input')

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))

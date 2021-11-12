def factorial(n):

    assert n >= 0, 'Input to factorial function was negative'

    if n <= 1: # If input to function is 1 or 0 return 1 since 1! = 1 and 0! = 1

        return 1

    else:

        return n*factorial(n-1) # recursive call to build stack of calls to the function factorial - notice the input

print(factorial(3))


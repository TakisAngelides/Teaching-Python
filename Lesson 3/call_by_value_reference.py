#Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”.
# In the event that you pass arguments like whole numbers, strings or tuples to a function,
# the passing is like call-by-value because you can not change the value of the immutable objects
# being passed to the function. Whereas passing mutable objects can be considered as call by reference
# because when their values are changed inside the function, then it will also be reflected outside
# the function.

# Scalars are call by value and the function does not change them (if a variable is immutable it is call by value)

# Lists are call by reference and the function changes them (if a variable is mutable it is call by reference)

# numpy arrays are call by reference since they are mutable, however, keep in mind that most numpy functions that
# transform arrays return new array objects, leaving the original unchanged.

import numpy as np

x = 1

list_x = [3, 4]

arr_y = np.array([9, 6]) # np.zeros(2) creates an array [0.0, 0.0] and gets mutated

str = 'Mike'

tup = (1,2,3)

def foo(num):

    num = 200

def foofoo(arr):

    arr[0] = 500

def foofoofoo(str_1):

    str_1 = 'Adam'

def foofoofoofoo(tup_1):

    tup_1 = (500,600,700)

foo(x)

foofoo(list_x)

foofoo(arr_y)

foofoofoo(str)

foofoofoofoo(tup)

print('x was originally 1 now it is: ', x)
print('Functions do not change scalars')

print('List list_x was originally [3, 4] now it is: ', list_x)
print('Functions do change lists')

print('List arr_y was originally [9, 6] now it is: ', list(arr_y))
print('Functions do not change original numpy arrays unless the array is created directly and not through a list')

print('String str was originally \'Mike\' now it is: ', str)
print('Functions do not change strings')

print('Tuple tup was originally (1,2,3) now it is: ', tup)
print('Functions do not change tuples')


# What if I want to pass a list into a function that takes a list and modifies it in some way but I want my original
# list to stay the same? We make a copy of the original list before calling the function and we call the function by
# passing the copy of the original list and not the original list itself.

list_y = [1, 2, 3]

list_y_copy = list_y.copy()

foofoo(list_y_copy)

print(list_y) # Original list stays the same

print(list_y_copy) # Copy gets changed as expected

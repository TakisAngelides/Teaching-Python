import numpy as np
from numpy import random
import time
import matplotlib.pyplot as plt
import datetime

array_1 = np.array([[1, 2], [3, 4]]) # returns numpy array

array_2 = np.array([2, 3, 4, 5])

print(array_1*3) # element wise multiplication by a single scalar value (in this case 3)

print(array_1 + array_2) # element wise addition

print(array_1*array_2) # element wise multiplication

print(array_1/array_2) # element wise division

print(array_1.shape) # returns how big is the array in each dimension (here it only has 1 dimension)

print(array_1.dtype) # returns the data type (dtype) of the elements in the array
#
print(array_1.size) # returns the size of the first dimension

print(array_2.sum()) # returns the sum of the elements of the array

print(array_1.argmax()) # returns the index of the maximum value

print(array_1.argmin())

array_3 = array_1.copy()
print(array_3) # returns a copy of the array


# Numpy arrays can only store a single type of data (cannot do multiple types in the same array)
# Lists and tuples can store many different types of data in the same variable
# Vectorisation = Use of more optimal and pre-compiled functions and mathematical operations
# on numpy arrays. The Output and Operations will speed-up when compared to simple non-vectorized operations.

# Example: Sum the integers from 1 to 1 000 000

t5 = datetime.datetime.now()
result = 0
for i in range(1, 1000001):
    result = result + i
t6 = datetime.datetime.now()
delta_t_slow = t6-t5
print('The sum of the first million integers using the for loop is', result, 'and it took', delta_t_slow.total_seconds(), 'seconds')

t7 = datetime.datetime.now()
array_3 = np.arange(1, 1000001, dtype = 'int64') # specify we want dtype (data type) integers of 64 bits
summation = np.sum(array_3)
t8 = datetime.datetime.now()
delta_t_fast = t8-t7
print('The sum of the first million integers using vectorisation is', summation, 'and it took', delta_t_fast.total_seconds(), 'seconds')

def slow_matrix_multiplication(m1, m2):

    result = np.zeros((m1.shape[0], m2.shape[1]))

    for i in range(m1.shape[0]):
        for j in range(m2.shape[1]):
            for col_m1 in range(m1.shape[1]):
                for row_m2 in range(m2.shape[0]):

                    result[i][j] = result[i][j] + m1[i][col_m1]*m2[row_m2][j]

    return result
#
def vectorised_matrix_multiplication(m1, m2):

    return np.matmul(m1, m2)
#
#
slow_time_list = []
fast_time_list = []
N_list = np.arange(2, 20)
same_result_list = np.array([])

for N in N_list:

    x = random.rand(N, N) # create an N x N random 2-dimensional array (matrix)

    y = random.rand(N, N) # create another an N x N random 2-dimensional array (matrix)

    t1 = time.time() # store the time written on the computer clock

    result_1 = slow_matrix_multiplication(x, y)

    t2 = time.time() # store the time written on the computer clock

    slow_time = t2-t1 # subtracting the two times gives the amount of time needed to do what is in between

    slow_time_list.append(slow_time) # put the amount of time needed to perform the function call into the list using append

    t3 = time.time()

    result_2 = vectorised_matrix_multiplication(x, y)

    t4 = time.time()

    fast_time = t4-t3

    fast_time_list.append(fast_time)

    np.append(same_result_list, result_1 == result_2)

# Plotting the data
plt.plot(N_list, slow_time_list, color = 'k', label = 'Slow')
plt.plot(N_list, fast_time_list, color = 'r', label = 'Fast')
plt.legend()
plt.ylabel('Time for calculation')
plt.xlabel('N')
plt.show()

print(same_result_list.all()) # checks if all elements of this list are true

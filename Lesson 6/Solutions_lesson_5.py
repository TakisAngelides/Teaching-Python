import numpy as np

"""

1) What is the remainder of the division 987654321/123456789?

2) Create a dictionary with 2 keys of type string 'a' and 'b', and set their values to a list of 2 boolean elements
   True and False.

3) Create a list of integers with duplicates in random order of magnitude and use the set function to remove duplicates
   and put the list in ascending order. Your final variable should be a list again.

4) Create a list of integers from 1 to 10. Write a for loop to loop over the list and if the element of the list is
   divisible by 2 or 3 remove it. If the element of the list is divisible by 2 and 4 replace that element with 0.

5) Write a function that returns the factorial of a non-negative integer using recursion.

6) Create a list with some elements of your choice. Write a function that uses recursion to print out the list element
   by element.

7) Import numpy. Create two matrices (ie 2-dimensional numpy arrays) and write a function to return their matrix
   multiplication.

8) Write to a text file 3 sentences where each sentence starts from a new line.

9) Use the text file you created in question 8 to read a text file and print its content line by line.

10) If you made it here well done!

"""

# Solutions

# ---------------------------------------------------------------------------------------------------------------------

# 1

print(987654321 % 123456789)

# ---------------------------------------------------------------------------------------------------------------------

# 2

dictionary_1 = {'a' : [True, False], 'b' : [True, False]}

# ---------------------------------------------------------------------------------------------------------------------

# 3

l_1 = [5,5,6,3,3,3,2,8,1,1,1,9]

tmp = set(l_1) # removes duplicates and puts list in ascending order returning a result of type set

l_1 = list(tmp) # cast the set to a list

# ---------------------------------------------------------------------------------------------------------------------

# 4

l_2 = [1,2,3,4,5,6,7,8,9,10]

tmp_list = []

for i in range(len(l_2)):

    element = l_2[i]

    if element % 2 == 0 or element % 3 == 0:

        # Here we cannot simply remove the element as it will change the length of the list and mess up the for
        # loop indexing. In other words remove will make the list shorter but the loop dummy variable i will go from
        # 0 to the original length of the list as instructed by range(len(l_2)) which we call with the original length
        # of the list. So here I am storing the elements I need to remove and will remove them outside the for loop.

        tmp_list.append(element)

    if element % 2 == 0 and element % 4 == 0:

        l_2[i] = 0

# Now I will remove the elements that needed to be removed

for element in tmp_list:

    if element in l_2: # need to check if the element is still in the list or has been converted to 0 by the second if statement in the for loop

        l_2.remove(element)

# ---------------------------------------------------------------------------------------------------------------------

# 5

def factorial(n):

    if n <= 1:

        return 1

    else:

        return n*factorial(n-1)

# ---------------------------------------------------------------------------------------------------------------------

# 6

l_3 = [1,2,3,4,5]

def recurse_list(lst, idx):

    if idx > len(lst)-1: # base case is when the index idx reaches the last index of our list lst

        pass # pass is just telling python to do nothing so here we will start going up the recursion you could have also written return

    else:

        print(lst[idx])
        recurse_list(lst, idx + 1)

recurse_list(l_3, 0)

# ---------------------------------------------------------------------------------------------------------------------

# 7

m1 = np.array([[1, 0], [0, 1]])

m2 = np.array([[1, 2], [3, 4]])

def matrix_multiplication(matrix_1, matrix_2):

    return np.matmul(matrix_1, matrix_2)

# ---------------------------------------------------------------------------------------------------------------------

# 8

with open('lesson_5_2.txt', 'w') as f:

    name = 'Takis Angelides'

    f.write('Hello friend\n')
    f.write('My name is\n')
    f.write(name)

# ---------------------------------------------------------------------------------------------------------------------

# 9

with open('lesson_5_2.txt', 'r') as f:

    line = f.readline()

    while line:

        print(line)

        line = f.readline()

# ---------------------------------------------------------------------------------------------------------------------


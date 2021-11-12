# Exercise 1: Write a for loop to print the first 5 integers from 0 to 4.

# Exercise 2: Create a list of the first 10 integers from 1 to 10 and iterate over the list to
# remove the even numbers.

# Exercise 3: Write a list comprehension to print the first 5 square integers (1,4,9,16,25).

# Exercise 4: Write a function that takes as input a list and prints the list element by element.
# Bonus: also output the list element by element in reverse order.

# Exercise 5: Write a function that takes a list and an integer index and returns the value of the
# neighbours. For example given the list [1,2,3,4,5] and the integer 2 which is the index for the value
# 3 in the list, the function should return [2,4] which are the neighbours of the value 3 at index 2. Hint:
# think also about the edge cases.

# Exercise 6: Write a function that takes a string and returns every other letter. For example given the
# string 'stars', it should return 'sas'.


























# Solutions

# 1

for i in range(5):
    print(i)

# 2

l = [element for element in range(1, 11) if element % 2 != 0]

# 3

l = [x*x for x in range(1, 6)]

# 4

def print_list(l):

    for i in range(len(l)):

        print(l[i])

def print_list_reverse(l):

    for i in range(len(l)-1, -1, -1):

        print(l[i])

# 5

def neighbours(l, i):

    if i == len(l) - 1:

        return [l[i-1]]

    elif i == 0:

        return [l[i+1]]

    else:

        return [l[i-1], l[i+1]]

# 6

def every_other(str):

    count = 0
    result = ''

    for letter in str:

        if count % 2 == 0:

            result = result + letter

        count += 1

    return result
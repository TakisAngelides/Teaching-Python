# string
# int
# float
# complex
# list
# tuple
# range
# dictionary
# set
# boolean

# ---------------------------------------------------------------------------------------------------------------------

# Examples of a strings

# Definition of Unicode: Unicode is a universal character encoding standard that assigns a code to every character and
# symbol in every language in the world

# Definition of string: sequence of Unicode characters wrapped inside single, double, or triple quotes)

# Essential a string is a bunch of characters in quotation marks, they are useful for storing words

string_1 = 'Mike'
string_2 = '34'
string_3 = ' '

print(string_1)

print('Here starts string_3 ->', string_3, '<- here ends string_3')

print(f'Here is string_3 -> {string_3} <- here ends string_3') # notice the f to the left of the quotation that allows the {} notation

print(type(string_3)) # string_3 is of class str ie it is of type string

print('Mike' + ' Adams') # concatenation of strings can be dones for example with the plus sign, concatenation means put two strings together

print(' '.join(['Mike', 'Adams'])) # another way to combine two strings is with the join function, join works as string.join(iterable), iterables are lists, tuples, strings

list_A = ['Hello', 'world', '.']
print(' '.join(list_A)) # Exercise how can I modify the above so that it outputs Hello world. rather than Hello world .

# ---------------------------------------------------------------------------------------------------------------------

# Examples of integers

x = 1
y = 2
z = x*y
print(z)
print(type(z)) # class int ie type integer

# --------------------------------------------------------------------------------------------------------------------

# Examples of float

q = 1.23
p = float(3)
print(p)
print(type(p))

# --------------------------------------------------------------------------------------------------------------------

# Examples of complex

w = 2
v = 3

r = complex(w, v) # r will be represented as 1 + 1j where j is the imaginary number in python

print(r)

print(type(r)) # class complex ie of type complex

print(r.real) # returns the real part of the complex number r

print(r.imag) # returns the imaginary part of the complex number r

# --------------------------------------------------------------------------------------------------------------------

# Examples of list

list_B = [1, 2, 3, 4]

list_C = ['Mike', 'Three']

list_D = ['Mike', 'Three', 'Yellow', 'two', 4, 6.54, r]

print(list_B[0]) # this is how we get elements from a list we specify the index and the index starts from 0

print(list_C[1])

print(type(list_D), type(list_D[2]), type(list_D[4]), type(list_D[-1])) # a list's last element can be indexed by -1 or its actual value in this case 6

print(list_D + list_A) # take list D and list A and merge them together into one big list (the + operation is overloaded as it will act differently depending on what it has to its left and right, this is called polymorphism)

print(list_B[1:3]) # prints values at indices starting from index = 1 and ending at index = 3-1 = 2

print(list_B[1:]) # prints values at indices starting from index = 1 and ending at the last index

list_B.append(5) # puts an element to the end of the list, this element can be another list

print(list_B)

print(list_D + [list_A])

list_D.append(list_A) # This does not achieve the same thing as list_D + list_A, see output on both cases, the append case achieves list_D + [list_A]

print(list_D)

list_B.remove(5)

# Below is a simple way to handle possible errors that might occur and in this way we prevent the program from terminating on the error
try:
    list_B.remove(6)
except:
    print('You tried to remove a value from list_B but that value was not in list_B in the first place')

print(list_B)

# ---------------------------------------------------------------------------------------------------------------------

# Examples of tuples

# The difference with lists is that tuples are immutable you cannot change their content once you define them

tuple_1 = (1,2,3,4) # it is a bunch of elements separated by a comma and enclosed by brackets

tuple_2 = ('Mike',) # For a 1 item tuple you need to include a comma at the end

not_tuple_2 = ('Mike')

not_tuple_2_str = 'Mike'

print(type(tuple_2))

print(type(not_tuple_2))

print(not_tuple_2 == not_tuple_2_str)

print(tuple_1[0])

try:
    # this will give an error saying TypeError: 'tuple' object does not support item assignment
    tuple_1[0] = -1
except:
    print('Tuples are immutable, you cannot change their content once you create them')

print(tuple_1)

# ---------------------------------------------------------------------------------------------------------------------

# Examples of range

range_1 = range(10) # default step to 1 and default start at 0
print(range_1)
print(list(range_1))

range_2 = range(0, 10)
print(range_2)

range_3 = range(5, 11)
print(range_3)

range_4 = range(-4, 3)
print(range_4)

range_5 = range(0, 10, 2) # start stop step_size correspond to 0 10 and 2 ie this will return 0,2,4,8
print(range_5)

range_6 = range(0, -10, -1)
print(list(range_6))

print(list(range(-5))) # Exercise why does this return the empty list, hint look at comment of first example and think of the stopping condition

# ---------------------------------------------------------------------------------------------------------------------

# Examples of dictionary

# Dictionary is a key -> value map

dictionary_A = {'Person 1' : 1.78, 'Person 2' : 1.65} # the keys are the strings Person 1 and Person 2 and point to the float values 1.78 and 1.65 respectively

print(dictionary_A.keys()) # prints the keys of the dictionary

print(type(dictionary_A))

print(type(dictionary_A.keys()))

print(list(dictionary_A.keys()))

print(type(list(dictionary_A.keys())))

items_A = dictionary_A.items() # this will be the values to which the keys point to ie 1.78 and 1.65

print(items_A)

print(type(items_A))

print(list(items_A))

# ---------------------------------------------------------------------------------------------------------------------

# Examples of set

# A set is like a list but it cannot contain two objects which are the same and is not mutable like a tuple

set_1 = {1, 2, 3}

print(set_1)

set_2 = {'Mike', 5, 1.89, (4, 'Adams')} # a list cannot be part of a set because lists are mutable, same goes with lists in tuples

print(set_2)

set_3 = set([1, 8, 1, 3, 2, 3, 5, 7, 7]) # set will remove duplicates and order the list in ascending order

print(set_3)

set_4 = set(['Mike', 'Andrew']) # it will order the names in alphabetical order

print(set_4)

# ---------------------------------------------------------------------------------------------------------------------

# Examples of boolean (bool type)

# Bool are expressions of True or False

boolean_1 = True

print(boolean_1)

print(type(boolean_1))

boolean_2 = False

print(boolean_2)

b_1 = 1

b_2 = 2

boolean_3 = b_2 > b_1

print(boolean_3)

boolean_4 = b_1 > b_2

print(boolean_4)

print(not 0) # double negative gives True, same as saying not False

print(not False) # same as above, this will give True

print(not True) # this will give False

list_E = [1, 2, 3]

boolean_5 = 1 in list_E

print(boolean_5)

boolean_6 = 1 not in list_E

print(boolean_6)


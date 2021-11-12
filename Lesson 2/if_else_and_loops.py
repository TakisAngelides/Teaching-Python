x = 5

#-------------------------------------------------------------------------------------------------------

if x > 4:
    print('x is greater than 4')
else:
    print('x is less than 4')

#-------------------------------------------------------------------------------------------------------

if x == 5:
    print('x is equal to 5')
else:
    print('x is not equal to 5')

#-------------------------------------------------------------------------------------------------------

if x > 10:
    print('x is greater than 10')
elif x < 1:
    print('x is less than 1')
else:
    print('x is between 2 and 9 inclusive')

#-------------------------------------------------------------------------------------------------------

name = 'Mike'

if name == 'Mike':
    print('The name is Mike')
else:
    print('The name is not Mike')

#-------------------------------------------------------------------------------------------------------

if name[0] == 'M':
    print('The first letter of name is M')
else:
    print('The first letter of name is not M')

#-------------------------------------------------------------------------------------------------------

flag = True

if flag:
    print('The flag is true')
else:
    print('The flag is false')

#-------------------------------------------------------------------------------------------------------

y = 0

if y:
    print('y is not 0')
else:
    print('y is 0')

#-------------------------------------------------------------------------------------------------------

z = 104

if z % x == 0:
    print('z is divisible by x')
else:
    print('z is not divisible by x')

#-------------------------------------------------------------------------------------------------------

colour = 'yellow'

if colour == 'black':
    print('Colour is black')
elif colour == 'red':
    print('Colour is red')
elif colour == 'yellow':
    print('Colour is yellow')
else:
    print('Colour is not black, red or yellow')

#-------------------------------------------------------------------------------------------------------

# Note: Python variables are scoped to the innermost function, class, or module in which they're assigned.
# Control blocks like if and while blocks don't count, so a variable assigned inside an if is still scoped
# to a function, class, or module.

w1, w2 = 3, 7

if w1 < w2:
    summation = w1 + w2
    w3 = sum
else:
    difference = w2 - w1
    w3 = difference

print('w3 is', w3)

#-------------------------------------------------------------------------------------------------------

if 5 % 2 == 0 or type(6 / 4) == int:
    print('5 is divisible by 2 or 6/4 is an integer')
else:
    print('5 is not divisible by 2 or 6/4 is not an integer')

if 10 / 5 == 2 and 9 % 2 == 0:
    print('10/5 is 2 and 9 is divisible by 2')
else:
    print('Either 10/5 is not 5 or 9 is not divisible by 2')

#-------------------------------------------------------------------------------------------------------

for i in range(10):
    print() # Prints from 0 to 9

for i in range(0, 15, 3):
    print(i) # Prints 0, 3, 6, 9, 12

for j in range(-3, 4, 1):
    print(j) # Prints from -3 to 3 in steps of 1

#-------------------------------------------------------------------------------------------------------

list_1 = ['blue', 'green', 'yellow', 'black']

for element in list_1:
    print(element)

for i in range(len(list_1)):
    print(list_1[i])

#-------------------------------------------------------------------------------------------------------

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        print('i =', i,'j =', j)

#-------------------------------------------------------------------------------------------------------

list_2 = [i*i for i in range(10)]

list_3 = []
for i in range(10):
    list_3.append(i**2)

print(list_2)
print(list_3)

#-------------------------------------------------------------------------------------------------------

word = 'iteration'

for letter in word:
    print(letter)

#-------------------------------------------------------------------------------------------------------

var_1 = 0
var_2 = 10

while var_1 < var_2:
    print(var_1) # Prints from 0 to 9
    var_1 += 1

#-------------------------------------------------------------------------------------------------------

flag = False

var_3 = 2
var_4 = 9

while not flag:
    if var_4 % var_3 == 0:
        flag = True
        print('While loop will terminate on', var_3)
    var_3 += 1

#-------------------------------------------------------------------------------------------------------

for i in range(10):

    if i > 5:

        print('i is greater than 5')

    else:

        print('i is less than 5')

#-------------------------------------------------------------------------------------------------------

list_4 = []
var_5 = 10

while not list_4:

    var_5 -= 1

    if var_5 == 0:

        list_4.append(var_5)

print(list_4)

#-------------------------------------------------------------------------------------------------------

# newlist = [expression for item in iterable if condition == True]

list_5    = [x*x for x in [4,5,6] if x % 2 == 0]

list_6 = [list_5[i] for i in range(len(list_5)) if list_5[i] % 3 == 0]

print(list_5)
print(list_6)

#-------------------------------------------------------------------------------------------------------


def addition(x, y):

    return x + y

def talk():

    print('Hello')

    return  # Since it returns nothing the type is 'NoneType'


print(type(talk()))


def fun(x, y = 3):

    return x*y


print(fun(3))
print(fun(3, 4))


def func(x, y, list_A, str_B, flag):

    """
    :param x: integer
    :param y: float
    :param list_A: list containing names as strings
    :param str_B: string
    :param flag: boolean
    :return: NoneType
    """

    z = x*y  # This ends up being a float

    if (str_B in list_A) or flag:

        w = z % 2

    else:

        w = z % 3

    print('w =', w)

    return


func(3, 1.5, ['George', 'Mike'], 'Mike', False)


def ball(mass = 2):

    def bounce(mass):

        height = 1/mass

        return height

    h = bounce(mass)

    return h*2


print(ball())

# A Python scope determines where in your program a name is visible

# Local scope

# The local scope or function scope is a Python scope created at function calls.
# Every time you call a function, you’re also creating a new local scope.

def square(base):
    result = base ** 2
    print(f'The square of {base} is: {result}')

square(10)

try:
    print(result) # result is not accessible from outside the function square where it is first declared
except:
    print('Result is not defined')

# Enclosing scope

# Enclosing or nonlocal scope is observed when you nest functions inside other functions.

def fun_1():

    def fun_2():
        x = 1

    try:
        print(x)
    except:
        print('x is not accessible outside the function it is defined in')

fun_1()

# Global scope

global_var = 3

def fun_3():

    global global_var

    global_var = global_var + 1

fun_3()
print('global_var value is: ', global_var)

# Built in scope

def fun_200():

    l = [1,2,3]

    def fun_300():

        print('Lenght of l: ', len(l))

    fun_300()

fun_200()

try:
    fun_300()
except:
    print('Function within a function is not accessible from outside the parent function')


# Treat args as a list

def my_sum(*args): # The name *args can be anything eg *my_arguments

    a = args[0][0]
    b = args[0][1]
    c = args[0][2]

    return a**a + c*b

my_sum((1,2,3))

# Treat kwargs as a dictionary

def merge(**kwargs):

    first_key_word_argument = kwargs['a']
    second_key_word_argument = kwargs['b']

    values = kwargs.values()

    return ' '.join(values)

print(merge(a = 'Hello', b = 'world.'))

def gravity(**kwargs):

    if 'g' in kwargs.keys():
        g = kwargs['g']
    else:
        g = 0

    return g

print(gravity(g = 9.81))

print(gravity(k = 3, T = 5.67, st = 'left'))







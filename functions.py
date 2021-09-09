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

# At each time you can only move one of the discs

# The discs have to be in decreasing radius from bottom to top (ie biggest on bottom smallest on top)

# You have 3 poles and every piece starts from pole A, the goal is to move everything to one of the other poles say pole C

def move(f, t):

    print(f'Move 1 disc from {f} to {t}.')


def hanoi(n, f, h, t):
    """
    :param n: Total number of discs to start with
    :param f: Initially all discs are on f tower (we will name this A ie f = 'A')
    :param h: This is the helper pole (we will name this B ie h = 'B')
    :param t: Thisis the target pole (we will name this C ie t = 'C')
    :return: We return print statements of the moves that solve the game
    """

    if n == 0:

        return

    else:

        hanoi(n-1, f, t, h)

        move(f, t)

        hanoi(n-1, h, f, t)


print(hanoi(4, 'A', 'B', 'C'))
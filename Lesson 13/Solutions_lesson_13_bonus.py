from random import choice, randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

# --------------------------------------------------------------------------------------------------------------------

# Exercises

# 1

# Build a rock paper scissors game using a random number generator.

# 2

# Build a random walk in 2D using a random number generator. This means you start from (x0, y0) where x0, y0
# are integers and generate random moves for moving left, right, up, down or diagonal for each step you take.
# You should plot the path at the end.

# --------------------------------------------------------------------------------------------------------------------

# Solutions

# --------------------------------------------------------------------------------------------------------------------

# 1

move = ['rock', 'paper', 'scissors']

player_1_move = choice(move)
player_2_move = choice(move)

def who_won(p1, p2):

    if p1 == 'rock':

        if p2 == 'paper':

            return f'Player 2 won with {p2} against player 1 with {p1}'

        elif p2 == 'rock':

            return f'It is a tie with both players drawing {p1}'

        else:

            return f'Player 1 won with {p1} against player 2 with {p2}'

    if p1 == 'paper':

        if p2 == 'paper':

            return f'It is a tie with both players drawing {p1}'

        elif p2 == 'rock':

            return f'Player 1 won with {p1} against player 2 with {p2}'

        else:

            return f'Player 2 won with {p2} against player 1 with {p1}'

    if p1 == 'scissors':

        if p2 == 'paper':

            return f'Player 1 won with {p1} against player 2 with {p2}'

        elif p2 == 'rock':

            return f'Player 2 won with {p2} against player 1 with {p1}'

        else:

            return f'It is a tie with both players drawing {p1}'

print(who_won(player_1_move, player_2_move))

# --------------------------------------------------------------------------------------------------------------------

# 2

def random_walk(x0 = 0, y0 = 0, steps = 5000):

    x = [x0] # will store all the x values of the walk
    y = [y0] # will store all the y values of the walk

    for step in range(steps):

        x.append(x[step] + randint(-1, 1)) # x_new = x_old + random move in x
        y.append(y[step] + randint(-1, 1)) # y_new = y_old + random move in y

    return x, y

x, y = random_walk() # Generate the whole random walk

# Plot the whole path - makes a good computational art

plt.plot(x, y)
plt.show()

# How to make an animation of this

fig = plt.figure() # create a figure object
ax = plt.axes(xlim = (min(x), max(x)), ylim = (min(y), max(y))) # create an axes object
plt.xticks([]) # no numbers on the x axis (empty list of numbers)
plt.yticks([]) # no numbers on the y axis
line, = ax.plot([], [], lw=1) # line is a plot object associated to the axes object, ax.plot() returns a tuple with one element. By adding the comma to the assignment target list, you ask Python to unpack the return value and assign it to each variable named to the left in turn.

def init(): # function to initialise the data of the first plot that would make the animation, it is initialised to empty lists ie no data
    line.set_data([], []) # set x and y data to the plot object we called line from above
    return line

x_list, y_list = [], [] # this will hold (accumulate) the data for each plot forming the animation

def animate(i): # this function updates the data of the plot that forms the animation, i is the index of the frame

    if i > len(x)-1: # if we have surpassed the biggest index in the x data list we pass ie do nothing since we plotted (animated) all the data we have
        pass
    else:
        x_list.append(x[i]) # append every 40 x data points to make the animation seem like it is going faster
        y_list.append(y[i])
        line.set_data(x_list, y_list) # update the data on the plot
    return line

anim = FuncAnimation(fig, animate, init_func=init, interval = 0.00001, repeat = False) # interval is delay between frames in milliseconds, repeat = False means when the animation data are finished do not repeat the animation
plt.show()

# --------------------------------------------------------------------------------------------------------------------

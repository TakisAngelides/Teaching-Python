from numpy import cos, sin, pi, sqrt, average
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

# --------------------------------------------------------------------------------------------------------------------

# We need to specify x0, y0, vx0, vy0, keep track of x, y, vx, vy and return x, y

dt = 0.0001 # time step

steps = 50000 # number of steps to perform

g = 9.8 # gravitational strength

k = 1 # strength of drag

m = 1 # mass

n = 1 # power law of drag with speed

v0 = 10 # initial speed

angle0 = 30 # initial angle with respect to the x-axis

x0, y0, vx0, vy0 = 0, 0, v0*cos(angle0*pi/180), v0*sin(angle0*pi/180) # in the cos and sin functions we pass radians = angle in degrees * pi / 180, this specify the initial position and velocity

x, y, vx, vy = [x0], [y0], [vx0], [vy0] # lists to hold the x,y positions and the v_x, v_y velocities

def integrate():

    for i in range(steps): # evolve in time the position and velocity as many times as specified by the number of steps

        x.append(x[i] + vx[i] * dt) # x_new = x_old + v_x * dt

        y_new = y[i] + vy[i] * dt # y_new = y_old + v_y * dt

        y.append(y_new)

        speed = sqrt(vx[i]**2 + vy[i]**2) # speed = sqrt(v_x**2 + v_y**2) = |v|, to be used below

        vx.append(vx[i] + (1/m) * dt * (-k * (speed**n) * vx[i]/speed)) # v_x_new = v_x + (1/m) * dt * F_x which implies F_x = -k * (|v|**n) * vx[i]/|v|)

        vy_new = vy[i] + (1/m) * dt * (-k * (speed**n) * vy[i]/speed - g) # v_x_new = v_x + (1/m) * dt * F_y which implies F_y = -k * (|v|**n) * vy[i]/|v| - g

        if (y[i] > 0) and (y_new < 0): # if y position was positive in the previous time step and negative in this time step then reverse the y velocity

            vy.append(-vy_new) # make the bounce on the ground at y = 0

        else:

            vy.append(vy_new)

    return x, y

pos_x, pos_y = integrate()

# --------------------------------------------------------------------------------------------------------------------

fig = plt.figure() # create a figure object
ax = plt.axes(xlim=(-0, 10), ylim=(0, 1)) # create an axes object
plt.xticks([]) # no numbers on the x axis (empty list of numbers)
plt.yticks([]) # no numbers on the y axis
line, = ax.plot([], [], lw=3) # line is a plot object associated to the axes object, ax.plot() returns a tuple with one element. By adding the comma to the assignment target list, you ask Python to unpack the return value and assign it to each variable named to the left in turn.

def init(): # function to initialise the data of the first plot that would make the animation, it is initialised to empty lists ie no data
    line.set_data([], []) # set x and y data to the plot object we called line from above
    return line

x_list, y_list = [], [] # this will hold (accumulate) the data for each plot forming the animation

def animate(i): # this function updates the data of the plot that forms the animation, i is the index of the frame

    if i*40 > len(x)-1: # if we have surpassed the biggest index in the x data list we pass ie do nothing since we plotted (animated) all the data we have
        pass
    else:
        x_list.append(x[i*40]) # append every 40 x data points to make the animation seem like it is going faster
        y_list.append(y[i*40])
        line.set_data(x_list, y_list) # update the data on the plot
    return line

anim = FuncAnimation(fig, animate, init_func=init, interval = 0.0000000001, repeat = False) # interval is delay between frames in milliseconds, repeat = False means when the animation data are finished do not repeat the animation
plt.show()

# --------------------------------------------------------------------------------------------------------------------

plt.plot(pos_x, pos_y)
plt.title(f'k = {k}, g = {g}, m = {m}, n = {n}, v0 = {v0}, angle0 = {angle0}')
plt.show()

# --------------------------------------------------------------------------------------------------------------------

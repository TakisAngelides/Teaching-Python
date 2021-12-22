import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

G = 1
M = 10
m = 1
dt = 0.0001
num_steps = 10000

def r(x,y):
    return np.sqrt(x**2+y**2) # this assumes the big attracting objectis at 0, 0

def a_x(x,y):
    return -G*M*x/(r(x,y)**3) # the x component of acceleration

def a_y(x,y):
    return -G*M*y/(r(x,y)**3) # the y component of acceleration

def leapfrog(x_0, y_0, vx_0, vy_0):

    x, y = np.zeros(num_steps), np.zeros(num_steps) # initialize numpy arrays which we called x and y that will hold the position data from time = 0 to the end
    vx, vy = np.zeros(num_steps), np.zeros(num_steps) # initialize numpy arrays which we called vx and vy that will hold the velocity data from time = 0 to the end
    x[0], y[0], vx[0], vy[0] = x_0, y_0, vx_0, vy_0 # the initial position and velocity are given as input to this function and here we put them in the arrays that will hold all the data from time = 0 to the end

    for i in range(num_steps-1): # each iteration of this for loop performs one time step integration using the leapfrog algorithm

        x[i + 1] = x[i] + vx[i] * dt + 0.5 * a_x(x[i], y[i]) * (dt ** 2)
        y[i + 1] = y[i] + vy[i] * dt + 0.5 * a_y(x[i], y[i]) * (dt ** 2)

        vx[i + 1] = vx[i] + 0.5 * (a_x(x[i], y[i]) + a_x(x[i + 1], y[i + 1])) * dt
        vy[i + 1] = vy[i] + 0.5 * (a_y(x[i], y[i]) + a_y(x[i + 1], y[i + 1])) * dt

    return x, y

x, y = leapfrog(x_0 = 1, y_0 = 0, vx_0 = 0, vy_0 = 1)

# plt.scatter(1,0, color = 'r')
# plt.scatter(0,0, color = 'yellow')
# plt.plot(x, y, color = 'k')
# plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(-0.5, 1.5), ylim=(-0.5, 0.5))
plt.scatter(0,0, color = 'yellow')
plt.xticks([])
plt.yticks([])
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

x_list, y_list = [], []

def animate(i):

    x_list.append(x[i*10])
    y_list.append(y[i*10])
    line.set_data(x_list, y_list)
    return line,

anim = FuncAnimation(fig, animate, init_func=init, interval = 0.0000000001, repeat = False)
plt.show()












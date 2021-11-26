from numpy import pi, sin, cos
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

steps = 100000
delta_t = 0.001
l = 1
m = 1
g = 9.8
theta_0, omega_0 = 160*pi/180, 0
theta = [theta_0]
omega = [omega_0]

def evolve():

    for t in range(steps):

        theta_new = theta[t] + omega[t] * delta_t

        if theta_new >= 2*pi:

            theta.append(0)

        else:

            theta.append(theta_new)

        omega_new = omega[t] - g*sin(theta[t])*delta_t/l

        omega.append(omega_new)

evolve()

fig = plt.figure()
ax = plt.axes(xlim = (-2, 2), ylim = (-2, 2))
plt.xticks([])
plt.yticks([])
plt.scatter(0, 0, color = 'yellow', marker = 'x')
x0 = [l*sin(theta[0])]
y0 = [-l*cos(theta[0])]
animation_plot = ax.scatter(x0, y0, s = 100, zorder = 1)
string, = ax.plot([0, x0[0]], [0, y0[0]], color = 'red', zorder = 0)


def update_animation_plot(i):

    t = theta[(i+1)*10]
    x = l*sin(t)
    y = -l*cos(t)
    animation_plot.set_offsets([x, y])
    string.set_data([0, x], [0, y])

    return string

anim = FuncAnimation(fig, update_animation_plot, interval = 0.000001)
plt.show()
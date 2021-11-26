from numpy import cos, sin, pi, sqrt, average
import matplotlib.pyplot as plt

# 1

# Generalise the code in project_with_drag.py to make plots of the trajectories of projectiles with many
# different drag strengths k and put them in the same plot.

# Solutions

# --------------------------------------------------------------------------------------------------------------------

def integrate(k):

    dt = 0.0001
    steps = 50000
    g = 9.8
    m = 1
    n = 1
    v0 = 10
    angle0 = 30
    x0, y0, vx0, vy0 = 0, 0, v0 * cos(angle0 * pi / 180), v0 * sin(angle0 * pi / 180)
    x, y, vx, vy = [x0], [y0], [vx0], [vy0]

    for i in range(steps):

        x.append(x[i] + vx[i] * dt)
        y_new = y[i] + vy[i] * dt
        y.append(y_new)
        speed = sqrt(vx[i]**2 + vy[i]**2)
        vx.append(vx[i] + (1/m) * dt * (-k * (speed**n) * vx[i]/speed))
        vy_new = vy[i] + (1/m) * dt * (-k * (speed**n) * vy[i]/speed - g)

        if (y[i] > 0) and (y_new < 0):
            vy.append(-vy_new)
        else:
            vy.append(vy_new)

    return x, y

k_list = [0, 0.5, 1]
max_x = [] # will store the maximum x distance the projectile travelled in the plotted trajectory

for k in k_list: # each time this for loop runs it calls plt.plot() with different data and because the plt.show() is outside the for loop it keeps accumulating plots on the same axes

    pos_x, pos_y = integrate(k)
    max_x.append(max(pos_x)) # max(list) gets the maximum element from the list input
    plt.plot(pos_x, pos_y, label = f'k = {k}')

plt.title('Projectiles with drag')
plt.xlim(0, min(max_x)) # set the x limits on the plot to be the minimum of the maximum x distances every projectile has travelled
plt.legend()
plt.show()

# --------------------------------------------------------------------------------------------------------------------




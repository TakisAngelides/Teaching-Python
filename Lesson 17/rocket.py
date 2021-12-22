import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

T = 100000
dt = 0.01
g = 9.81
L = 2*10**4 # how many kg per second to lose on fuel ejection
v_ej = 1 # speed of fuel as it leaves the rocket relative to the rocket
C_D = 0.05 # air resistance coefficient
rho_0 = 1.225 # density of air at sea level
A = np.pi*(22)**2 # cross sectional area of rocket CRS dragon of space X falcon 9
y_ground = 0 # ground is at y = 0
y_space = 110000 # atmosphere ends at y = 110000

def force(m, pos_vec, vel_vec, flag, flag_escape):

    v_hat = vel_vec/np.linalg.norm(vel_vec)

    W = -m*g*np.array([0, 1])
    AR = -0.5*rho_0*np.exp(-pos_vec[1])*C_D*A*np.linalg.norm(vel_vec)**2*v_hat
    T = L*v_ej*v_hat # thrust is dm_rocket/dt * v_ej but dm_rocket/dt is -L and v_ej is |v_ej|(-v_hat)

    if flag_escape: # if the rocket escaped earths atmosphere there is no external force and thrust is switched off

        return np.array([0, 0])

    if not flag: # if the fuel has not ran out yet

        return W + AR + T

    else:

        return W + AR # L is now 0

def integrate():

    m_rocket = 3 * 10 ** 6  # initial mass of rocket
    ejected_mass = 0  # initial mass of ejected fuel

    pos = np.zeros((T, 2)) # will hold all data of the position vector
    vel = np.zeros((T, 2)) # will hold all data of the velocity vector
    speed = np.zeros(T) # will hold all data of the speed
    fuel_left = np.zeros(T) # will hold all data of the remaining fuel
    total_fuel_mass = m_rocket*0.9
    fuel_left[0] = total_fuel_mass
    pos[0] = np.array([0, y_ground])
    y_initial_speed = 1000 # 750 # 1000 # 750 # 2500 # speed in meters per second
    vel[0] = np.array([5, y_initial_speed])
    speed[0] = np.linalg.norm([0, y_initial_speed])

    flag = False # if fuel runs out set this to true and switch off thrust in force function
    flag_escape = False # if we reach a certain height we have escaped earth atmosphere and no force acts on the rocket as we also switch off thrust

    for t in range(1, T):

        pos[t] = pos[t-1] + vel[t-1]*dt # update position
        vel[t] = vel[t-1] + force(m_rocket, pos[t-1], vel[t-1], flag, flag_escape)*dt/m_rocket # update velocity

        if not flag: # if we have not ran out of fuel yet
            m_rocket = m_rocket - L*dt # reduce the mass of the rocket lost to ejected fuel
            ejected_mass = ejected_mass + L*dt # increase the mass of ejected fuel
            if not flag_escape:
                fuel_left[t] = fuel_left[t - 1] - L * dt
            else:
                fuel_left[t] = fuel_left[t-1]

        if ejected_mass >= total_fuel_mass: # we ran out of fuel

            flag = True

        if pos[t][1] > y_space: # we have escaped earths atmosphere

            flag_escape = True

        if pos[t][1] < y_ground: # we have crashed to ground

            break

        speed[t] = np.linalg.norm(vel[t])

    return pos, speed, fuel_left

data, speed, fuel_left = integrate()

fig = plt.figure()
max_y = max(data.transpose()[1])
max_x = max(data.transpose()[0])
min_x = min(data.transpose()[0])
if max_y < y_space:
    ax = plt.axes(xlim = (min_x-1, max_x+1),ylim=(y_ground, y_space + 1))  # y limits of the figure are from y = 0 to y_space + 1
else:
    ax = plt.axes(xlim = (min_x-1, max_x+1),ylim = (y_ground, y_space*2)) # y limits of the figure are from y = 0 to max y reached by rocket
plt.hlines(0, min_x-1, max_x+1, color = 'green', linewidth = 5) # make a plot of a horizontal line at y = 0 from min x to max x representing the ground
plt.hlines(y_space, min_x-1, max_x+1, color = 'r', linewidth = 5, zorder = 0) # represents the max height of atmosphere
animation_plot = ax.scatter(data[0][0], data[0][1], s = 100)

def update_animation_plot(i):

    skip = 50
    idx = (i+1)*skip
    scatter_point = data[idx]
    if scatter_point[1] <= y_ground:
        print('Rocket has crashed.')
        quit()
    animation_plot.set_offsets(scatter_point)
    plt.legend([y_ground, y_space, f'y = {data[idx][1]:.0f}\nSpeed = {speed[idx]:.0f}\nFuel = {fuel_left[idx]:.0f}'])

    return animation_plot

anim = FuncAnimation(fig, update_animation_plot, interval = 0.0000000001, repeat = False)
plt.show()

from numpy import random as rdm
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
plt.style.use('dark_background')

class Particle():

    def __init__(self, r, m, x, y, vx, vy):

        self.r = r
        self.m = m
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])

class Box():

    def __init__(self, lx, ly, ux, uy, N, r, m):

        self.lx = lx
        self.ly = ly
        self.ux = ux
        self.uy = uy
        self.N = N
        self.particles_list = []
        speed = 10 # speed range to initialize each particle in
        eps = 0.1 # just a distance to initialize position of each particle away from walls
        for _ in range(N):
            self.particles_list.append(Particle(r, m, rdm.uniform(lx+eps, ux-eps), rdm.uniform(ly+eps, uy-eps), rdm.uniform(-speed, speed), rdm.uniform(-speed, speed)))

lx, ly, ux, uy = -1, -1, 1, 1 # limits of box
N = 3 # number of particles
iterations = 5000 # number of times to make a position update for the simulation
r = 0.02 # radius of particles, this is fixed to correspond to the plot size of the scatter plot below
m = 1 # mass of particles
box = Box(lx, ly, ux, uy, N, r, m) # create box object

dt = 0.001 # time step for each update of position

position_data = [[] for i in range(box.N)] # will hold the position of each particle

def check_collision(idx): # check if the particle has collided with a wall or another particle

    particles_list = box.particles_list # list of particles in the box
    particle_1 = particles_list[idx] # this is the particle we want to check if it collided

    if (particle_1.pos[0] + r > box.ux or particle_1.pos[0] - r < box.lx):

        # if the particle has collided with a wall we reverse its velocity in the x direction

        particle_1.vel[0] = -particle_1.vel[0]

    if (particle_1.pos[1] + r > box.uy or particle_1.pos[1] - r < box.ly):

        # if the particle has collided with a wall we reverse its velocity in the y direction

        particle_1.vel[1] = -particle_1.vel[1]

    for i in range(len(particles_list)): # loop over all particles

        if idx == i: # if the index corresponds to particle_1 then skip to the next index (a particle cannot collide with itself)

            continue

        elif np.linalg.norm(particle_1.pos-particles_list[i].pos) <= 2*r: # if the distance between particle_1 and another particle is less than 2r it means they collided (here you can generalise it to different radii for each particle)

            # we go to the zero momentum frame and update the velocities of each particle in the collision

            particle_2 = particles_list[i]

            m1 = particle_1.m
            m2 = particle_2.m

            V_ZMF = (m1*particle_1.vel + m2*particle_2.vel)/(m1 + m2)

            particle_1.vel = -particle_1.vel + 2*V_ZMF
            particle_2.vel = -particle_2.vel + 2*V_ZMF

def simulate():

    particles_list = box.particles_list # list of particles in the box

    for t in range(iterations):

        for i in range(len(particles_list)): # loop over all particles

            check_collision(i)  # check if the particle that corresponds to index i in the list of particles has collided

            particle = particles_list[i] # set a variable called particles to the object in the list of particles

            position_data[i].append(particle.pos)  # put the position in the data which we will plot later

            particle.pos = particle.pos + particle.vel*dt # update its position using x_new = x_old + v*dt


simulate()

# make the animation using FuncAnimation

fig = plt.figure() # initialize a figure object in which we will create an axes object to plot in
ax = plt.axes(xlim=(box.lx, box.ux), ylim=(box.ly, box.uy)) # initialize an axes object on which we will plot

# remove numbers from the axes

plt.xticks([])
plt.yticks([])

# x and y positions of all particles at time t = 0

x = [position_data[i][0][0] for i in range(box.N)]
y = [position_data[i][0][1] for i in range(box.N)]

# make a scatter plot of the initial positions, this will be the plot we will be changing to make the animation

scatter_plot = ax.scatter(x, y, color = 'green', s = 70) # [all particles][t = 0][x or y]

def animate(i): # function that updates the scatter plot using the positions of the next time step

    # this function is called by FuncAnimation below and each time its called the index i in the input is automatically incremented by 1

    if i > iterations-1: # if there is no more data to plot stop the whole file and exit
        quit()

    data = [position_data[j][i+1] for j in range(box.N)] # i starts from 0 by FuncAnimation and since we already plotted above the time 0 we start from i+1
    scatter_plot.set_offsets(data) # update the scatter plot
    return scatter_plot

animation = FuncAnimation(fig, animate, interval = 1, repeat = True) # function that makes the animation, interval is the microseconds between frames
plt.show() # we call this to open the window of the plot
# animation.save('boxed_particles.gif', writer = 'pillow') # a way to save the animation as a gif

import numpy as np
from numpy import pi
from random import uniform
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

throws = 10000 # number of throws per experiment
experiments = 400 # repeat the whole process this many times and take the average number of hits at the end
hits = np.zeros(experiments) # store hits at the end of each experiment

for experiment in range(experiments):

    x_list = []
    y_list = []

    for throw in range(throws):

        x = uniform(0, 1) # pick x with uniform probability from 0 to 1
        y = uniform(0, 1) # pick y with uniform probability from 0 to 1

        x_list.append(x)
        y_list.append(y)

        if (x**2+y**2)**(1/2) <= 1: # if the point (x, y) lies within the quadrant of the circle it counts as a hit

            hits[experiment] += 1 # increment the number of hits by one

    fig = plt.figure()
    ax = plt.axes(xlim = (0, 1), ylim = (0, 1))
    scatter_plot = plt.scatter(x_list[0], y_list[0], marker = 'x', color = 'k')

    phi = np.linspace(0, np.pi/2)
    x_circle = np.cos(phi)
    y_circle = np.sin(phi)

    quadrant_of_circle = ax.plot(x_circle, y_circle, color = 'r')

    data_acc = [[x_list[0], y_list[0]]]

    def update(i):

        data_acc.append([x_list[i+1], y_list[i+1]])
        scatter_plot.set_offsets(data_acc)

        return scatter_plot

    animation = FuncAnimation(fig, update, repeat = False, interval = 1)
    plt.title(f'Experiment number: {experiment}')
    plt.show()

print(4*np.average(hits)/throws, pi) # take the final result to be 4 times the average number of hits out of all the experiments divided by the total number of throws


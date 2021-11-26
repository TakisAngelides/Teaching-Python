import numpy as np
from numpy import pi
from random import uniform

throws = 10000 # number of throws per experiment
experiments = 400 # repeat the whole process this many times and take the average number of hits at the end
hits = np.zeros(experiments) # store hits at the end of each experiment

for experiment in range(experiments):

    for throw in range(throws):

        x = uniform(0, 1) # pick x with uniform probability from 0 to 1
        y = uniform(0, 1) # pick y with uniform probability from 0 to 1

        if (x**2+y**2)**(1/2) <= 1: # if the point (x, y) lies within the quadrant of the circle it counts as a hit

            hits[experiment] += 1 # increment the number of hits by one

print(4*np.average(hits)/throws, pi) # take the final result to be 4 times the average number of hits out of all the experiments divided by the total number of throws
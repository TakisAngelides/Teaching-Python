import random
import numpy as np
from numpy import pi

throws = 10000
experiments = 100
hits = np.zeros(experiments)

for experiment in range(experiments):
    print(experiment)
    for throw in range(throws):

        x = random.random()
        y = random.random()

        if (x**2+y**2)**(1/2) <= 1:

            hits[experiment] += 1

print(4*np.average(hits)/throws, pi)
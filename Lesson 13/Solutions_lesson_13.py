from random import uniform
import numpy as np

# --------------------------------------------------------------------------------------------------------------------

# Exercises

# --------------------------------------------------------------------------------------------------------------------

# 1

# Find the volume of a ball of radius 0.5 using hit or miss Monte Carlo.

# --------------------------------------------------------------------------------------------------------------------

# Solutions

# --------------------------------------------------------------------------------------------------------------------

# 1

# We imagine a ball centered at (0, 0, 0) in an x, y, z coordinate system. We will generate random points within the
# unit cube and check if the point lies within the ball using x**2 + y**2 + z**2 <= r**2.

def volume_of_unit_sphere(throws = 10000, experiments = 100):

    hits = np.zeros(experiments)

    for experiment in range(experiments):

        print(experiment)

        for throw in range(throws):

            pos = np.array([uniform(-0.5, 0.5), uniform(-0.5, 0.5), uniform(-0.5, 0.5)])

            if np.linalg.norm(pos) <= 0.5:

                hits[experiment] += 1

    return np.average(hits)/throws

print(volume_of_unit_sphere(), 4*np.pi*(0.5)**3/3)

# --------------------------------------------------------------------------------------------------------------------



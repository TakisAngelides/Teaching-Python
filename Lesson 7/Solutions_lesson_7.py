import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d # for 3D plots

# Questions:

# 1

# Make a plot of the function y = sin(1/x). x should have 10 000 points between -1 and 1.

# Hint: use linspace from numpy to create x.

# 2

# Make a 3D surface plot of a sphere of radius 1 centered at 0.

# 3

# Create a vector plot with all arrows having length 1 and pointing to the right.








# Solutions:

# 1

x = np.linspace(-1, 1, 10000)
y = np.sin(1/x)

plt.plot(x, y)
plt.show()

# 2

r = 1

# phi goes from 0 to 2pi and theta goes from 0 to pi in order to parameterise the whole sphere

phi = np.linspace(0, 2*np.pi, 1000)
theta = np.linspace(0, np.pi, 1000)

# make the phi and theta into a grid so that at each point of the grid we specify the value z

phi, theta = np.meshgrid(phi, theta)

# change the grid positions from angular coordinates to cartesian coordinates

x = np.cos(phi)*np.sin(theta)
y = np.sin(phi)*np.sin(theta)

# for each point on the grid we plot the value of z

z = np.cos(theta)

# create an axes object we call it ax but we can name it whatever we want as is always the case with naming variables

ax = plt.axes(projection = '3d')

ax.plot_surface(x, y, z, alpha = 0.5) # 3D surface plot

plt.show() # remember to call this in order for the plot window to actually open

# 3

x = np.linspace(-1, 1)
y = np.linspace(-1, 1)

X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()

U, V = X/X, Y*0

print(U.shape, V.shape)

ax.quiver(X, Y, U, V)

plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d # for 3D plots

#------------------------------------------------------------------------------------------------ 2D Line plot

x = np.linspace(-100, 100, 1000)
y = np.sin(x)

plt.plot(x, y, color = 'k', alpha = 1, markersize = 1, linestyle = '-') # alpha = 0 transparent and alpha = 1 totally opaque
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('y(x) = sin(x)')
plt.xlim([-8, 10]) # limits on the x-axis values
plt.ylim([-1.5, 2])
plt.show()

#------------------------------------------------------------------------------------------------ Bar plot

x = np.arange(0, 3.7, step = 0.1) # returns evenly spaces values within a given interval the upper limit is not inclusive
y = np.exp(-(x-1.8)**2) # vectorisation, this will evaluate for all values of x without explicit for loop

plt.bar(x, y) # bar plot
plt.show()

#------------------------------------------------------------------------------------------------ 3D Line, Scatter plots

# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html - a tutorial on 3D

fig = plt.figure()
ax = plt.axes(projection = '3d')

x = np.linspace(0, 15, 100)
y = np.sin(x)
z = np.cos(x)
ax.plot3D(x, y, z, color = 'k') # continuous line plot in 3D
ax.scatter3D(x, y, z, color = 'r', s = 4.5) # scattered points in 3D
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('z')
plt.show()

#------------------------------------------------------------------------------------------------ Surface plots

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

# Meshgrid intuition: https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig_1 = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50) # contour plot in 3D - the lines of equal height of a mountain for example
# ax.plot_wireframe(X, Y, Z, color='black')
# ax.plot_surface(X, Y, Z, alpha = 0.5) # continuous surface in 3D
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

#------------------------------------------------------------------------------------------------ Quiver vector plot

fig_2, (ax_1, ax_2) = plt.subplots(1, 2, figsize=(7, 7)) # create a figure object and a set of subplots - see documentation of subplots for how to add subplots
x = np.arange(-2, 2, 0.2)
y = np.arange(-2, 2, 0.2)

X, Y = np.meshgrid(x, y)
u = np.cos(X)*Y
v = np.sin(Y)*Y

n = -2
color_array = np.sqrt(((v-n)/2)**2 + ((u-n)/2)**2)

ax_1.quiver(X, Y, u, v, color_array) # vector plot - each point of the plot has a vector
ax_2.plot(x, y) # second subplot in the same figure
plt.show()

#------------------------------------------------------------------------------------------------

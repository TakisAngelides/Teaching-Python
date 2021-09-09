import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d # for 3D plots

# TODO: Remove links after you comment up the code
# TODO: Understand the code here better

#------------------------------------------------------------------------------------------------ 2D Line plot

# x = np.linspace(-100, 100, 1000)
# y = np.sin(x)
#
# plt.plot(x, y, color = 'k', alpha = 1, markersize = 1, linestyle = '-')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('y(x) = sin(x)')
# plt.xlim([-8, 10])
# plt.ylim([-1.5, 2])
# plt.show()

#------------------------------------------------------------------------------------------------ Bar plot

# x = np.arange(0, 3.7, step = 0.1)
# y = np.exp(-(x-1.8)**2)
#
# plt.bar(x, y)
# plt.show()

#------------------------------------------------------------------------------------------------ 3D Line, Scatter plots

# TODO: Remove
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

# fig = plt.figure()
# ax = plt.axes(projection = '3d')
#
# x = np.linspace(0, 15, 100)
# y = np.sin(x)
# z = np.cos(x)
# ax.plot3D(x, y, z, color = 'k')
# ax.scatter3D(x, y, z, color = 'r', s = 4.5)
# plt.xlabel('x')
# plt.ylabel('y')
# ax.set_zlabel('z')
# plt.show()

#------------------------------------------------------------------------------------------------ Surface plots

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))
#
# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
#
# # TODO: Remove
# # Meshgrid intuition: https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy
#
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# # ax.contour3D(X, Y, Z, 50)
# ax.plot_wireframe(X, Y, Z, color='black')
# ax.plot_surface(X, Y, Z, alpha = 0.5)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z');
# plt.show()

#------------------------------------------------------------------------------------------------ Quiver vector plot

# fig, ax = plt.subplots(figsize=(7,7))
# x = np.arange(0,2.2,0.2)
# y = np.arange(0,2.2,0.2)
#
# X, Y = np.meshgrid(x, y)
# u = np.cos(X)*Y
# v = np.sin(y)*Y
#
# n = -2
# color_array = np.sqrt(((v-n)/2)**2 + ((u-n)/2)**2)
#
# ax.quiver(X, Y, u, v, color_array)
# plt.show()

#------------------------------------------------------------------------------------------------

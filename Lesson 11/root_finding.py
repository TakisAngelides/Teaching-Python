from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def f(x): # function to find its roots

    return x**2 - 4

initial_guess = np.array([-1, 1]) # initial guess of where the two roots of the function are

roots = fsolve(f, initial_guess) # compute the roots of function f

print(roots)

# plot the function f

x = np.linspace(-10, 10)
plt.plot(x, f(x), color = 'k', label = 'f(x) = x*x - 4', zorder = 0) # label will appear in the legend which is the box next to the graph telling us which plot is which, zorder specifies which graph to lie on top of which
plt.grid()

# plot the roots of the function f

for root in roots:
    plt.scatter(root, f(root), marker = 'x', color = 'r', zorder = 1, s = 100, label = 'Roots of f(x) = x*x - 4') # s is the size of the marker

def g(x): # function to find intersection with f

    return x + 5

# plot the function g

plt.plot(x, g(x), color = 'orange', zorder = 2, label = 'g(x) = x + 5')
plt.ylim(-5, 10)

def h(x): # function which has its roots at the intersection of functions f and g

    return f(x)-g(x)

initial_guess = np.array([-1, 1]) # initial guess of where the roots of h are

roots = fsolve(h, initial_guess) # compute the roots of h which are the points of intersection of f with g

# plot the intersection points of f with g

for root in roots:
    plt.scatter(root, f(root), marker = 'x', color = 'blue', zorder = 3, s = 100, label = 'Intersection points\nh(x) = f(x) - g(x) = 0') # the label will appear in the legend, the characte \n tells the string to go to the next line

plt.legend() # the legend is the box that appears next to the graph and tells us what the label of each plot is
plt.show()


